import cv2
import mediapipe as mp
import numpy as np
from stats import *
from PIL import ImageFont, ImageDraw, Image
import pyttsx3

class PoseDetector:
    mpDraw = mp.solutions.drawing_utils
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()

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
            self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS, landmark_drawing_spec=None)
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


    def findPosition(self, img, side, draw=True):
        pl_list = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                pl_list.append([id, cx, cy])
                if draw and id in PRINT_PARTS[side]:
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

        ### Put angle on photo
        if correct_angle_min < angle < correct_angle_max:
            angle_text = 'OK'
        else:
            angle_text = self.text(positions[A], positions[B], positions[C], correct_angle_min, angle)

        color = GREEN if correct_angle_min < angle < correct_angle_max else RED
        place = (b[0], b[1] + 10) if pose else (b[0], b[1] - 10)

        fontpath = "./simsun.ttc"  # the font that has this "º" symbol
        font = ImageFont.truetype(fontpath, 32)
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text(place, angle_text, font=font, fill=color)

        # cv2.putText(img, angle_text, place, cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        img = np.array(img_pil)
        return img

    def runDetector(self, path, side, position, live=False, scale_percent=30):
        video = 0 if live else path
        cap = cv2.VideoCapture(video)

        while True:
            success, image = cap.read()
            if not success:
                self.run_voice('end')
                break

            # Resize image
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)
            dim = (width, height)
            img = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

            img = self.findPose(img)
            positions = self.findPosition(img, side)

            if len(positions) == 0:
                print('No pose landmarks found')
                break

            for angles in position:
                img = self.calculate_angle(img, positions, *angles)

            cv2.imshow('Image', img)
            cv2.waitKey(1)

    def run_voice(self, sentance):
        synthesizer = pyttsx3.init()
        synthesizer.say(sentance)
        synthesizer.runAndWait()
        synthesizer.stop()

if __name__ == '__main__':
    position = warrior_l
    path = '../videos/warrior_l.mp4'
    side = path[-5]
    while True:
        PoseDetector().runDetector(path, side, position, scale_percent=50)
