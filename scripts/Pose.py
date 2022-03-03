import cv2
import mediapipe as mp
import time
import numpy as np
from stats import *


class PoseDetector:
    mpDraw = mp.solutions.drawing_utils
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()

    def __int__(self, mode=False, upBody=False, smooth=True,
                detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks and draw:
            self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        pl_list = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                pl_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        return pl_list

    def calculate_angle(self, img, positions, A, B, C, correct_angle):

        ### Calculate angles
        a = np.array(positions[A][1:])
        b = np.array(positions[B][1:])
        c = np.array(positions[C][1:])

        BA = a - b
        BC = c - b

        cosine_angle = np.dot(BA, BC) / (np.linalg.norm(BA) * np.linalg.norm(BC))
        angle = int(np.degrees(np.arccos(cosine_angle)))

        ### Put angle on photo
        angle_text = str(angle)
        color = GREEN if 0.8 * correct_angle<angle<1.2 * correct_angle else RED
        cv2.putText(img, angle_text, (b[0] - 30, b[1]), cv2.FONT_HERSHEY_COMPLEX, 0.6, color, 2)

        return img

    def runDetector(self, path, position, live=False, scale_percent=30):

        video = 0 if live else path
        cap = cv2.VideoCapture(video)
        pTime = 0

        while True:
            success, image = cap.read()
            if not success: break

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

            fps = int(1 / (time.time() - pTime))
            pTime = time.time()
            cv2.putText(img, str(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, BLUE, 2)

            for angles in position:
                img = self.calculate_angle(img, positions, *angles)

            cv2.imshow('Image', img)
            cv2.waitKey(1)


if __name__ == '__main__':
    detector = PoseDetector()
    path = '../videos/warrior1.mp4'
    while True:
        detector.runDetector(path, warrior, scale_percent=50)
