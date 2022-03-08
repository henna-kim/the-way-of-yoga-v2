import time
import cv2
import mediapipe as mp
import numpy as np
from pose.stats import *
from PIL import ImageFont, ImageDraw, Image
import pyttsx3


class PoseDetector:
    mpDraw = mp.solutions.drawing_utils
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()
    arrows = []
    first_time = True
    speech = {
        '↓': 'down',
        '↑': 'up',
        '←': 'left',
        '→': 'right',
        'OK': ''
    }

    def __int__(self, side, mode=False, upBody=False, smooth=True,
                detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.side = side

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks and draw:
            self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS,
                                       landmark_drawing_spec=None)
        return img

    def text(self, A, B, C, correct_angle_min, angle):
        ver = A[0] - C[0]
        hor = A[1] - C[1]

        if ver > hor:
            if B[1] > A[1]:
                # if angle < correct_angle_min:
                return '→'
            else:
                if angle < correct_angle_min:
                    return '→'
                else:
                    return '←'

        else:
            if (B[0] < A[0] and angle <= 90) or (B[0] > A[0] and angle > 90):
                if angle < correct_angle_min:
                    return '↓'
                else:
                    return '↑'
            else:
                if angle < correct_angle_min:
                    return '↑'
                else:
                    return '↓'

    def findPosition(self, img, draw=True):
        pl_list = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                pl_list.append([id, cx, cy])
                if draw and id in PRINT_PARTS:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        return pl_list

    def calculate_angle(self, img, positions, A, B, C, correct_angle_min, correct_angle_max, pose):

        ### Calculate angles
        a = np.array(positions[A][1:])
        b = np.array(positions[B][1:])
        c = np.array(positions[C][1:])

        BA = a - b
        BC = c - b

        cosine_angle = np.dot(BA, BC) / (np.linalg.norm(BA) * np.linalg.norm(BC))
        cosine_angle = cosine_angle if -1 < cosine_angle < 1 else int(cosine_angle)
        degrees = np.arccos(cosine_angle)
        angle = int(np.degrees(degrees))
        textes = []
        ### Put angle on photo
        if correct_angle_min < angle < correct_angle_max:
            angle_text = 'OK'
        else:
            angle_text = self.text(positions[A], positions[B], positions[C], correct_angle_min, angle)

        textes.append(angle_text)
        color = GREEN if correct_angle_min < angle < correct_angle_max else RED
        place = (b[0], b[1] + 10) if pose else (b[0], b[1] - 10)

        font = ImageFont.truetype("./simsun.ttc", 32)
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text(place, angle_text, font=font, fill=color)

        img = np.array(img_pil)
        return img, textes

    def runDetector(self, position, path=None, live=True, scale_percent=30):
        video = 0 if live else path
        cap = cv2.VideoCapture(video)
        start = time.time()

        while True:
            success, image = cap.read()
            if not success: break

            elapsed = time.time() - start
            checking = elapsed

            if checking > 3:
                if not all(x is None for x in self.arrows):
                    self.run_voice(self.arrows)
                start = time.time()
                self.arrows = []
                self.first_time = True

            # Resize image
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)
            dim = (width, height)
            img = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

            img = self.findPose(img)
            positions = self.findPosition(img)

            if len(positions) == 0:
                print('No pose landmarks found')
                break

            temps = []
            for angles in position:
                img, temp = self.calculate_angle(img, positions, *angles)
                temps.append(temp)

            if self.first_time:
                self.arrows = temps
                self.first_time = False
            else:
                for i, temp in enumerate(temps):
                    if self.arrows[i] != temp:
                        self.arrows[i] = None

            cv2.imshow('Image', img)
            cv2.waitKey(1)

    def run_voice(self, lists):
        for i, move in enumerate(lists):
            if move in [['↓'], ['↑'], ['←'], ['→']]:
                synthesizer = pyttsx3.init()
                synthesizer.say('Move your')
                synthesizer.runAndWait()
                synthesizer.stop()
                number = info_parts['warrior'][i]
                body_name = body_part[number]
                synthesizer.say(body_name)
                synthesizer.runAndWait()
                synthesizer.stop()
                synthesizer.say(self.speech[move[0]])
                synthesizer.runAndWait()
                synthesizer.stop()


if __name__ == '__main__':
    position = warrior3
    path = '../videos/warrior3.mp4'
    while True:
        PoseDetector().runDetector(position)
