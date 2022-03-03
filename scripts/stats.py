NOSE = 0
LEFT_EYE_INNER = 1
LEFT_EYE = 2
LEFT_EYE_OUTER = 3
RIGHT_EYE_INNER = 4
RIGHT_EYE = 5
RIGHT_EYE_OUTER = 6
LEFT_EAR = 7
RIGHT_EAR = 8
MOUTH_LEFT = 9
MOUTH_RIGHT = 10
LEFT_SHOULDER = 11
RIGHT_SHOULDER = 12
LEFT_ELBOW = 13
RIGHT_ELBOW = 14
LEFT_WRIST = 15
RIGHT_WRIST = 16
LEFT_PINKY = 17
RIGHT_PINKY = 18
LEFT_INDEX = 19
RIGHT_INDEX = 20
LEFT_THUMB = 21
RIGHT_THUMB = 22
LEFT_HIP = 23
RIGHT_HIP = 24
LEFT_KNEE = 25
RIGHT_KNEE = 26
LEFT_ANKLE = 27
RIGHT_ANKLE = 28
LEFT_HEEL = 29
RIGHT_HEEL = 30
LEFT_FOOT_INDEX = 31
RIGHT_FOOT_INDEX = 32

### Colors
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

### Positions
warrior_l = [(LEFT_HIP, LEFT_KNEE, LEFT_ANKLE, 120, 180, 1),
           (LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE, 90, 120, 1),
           (RIGHT_SHOULDER, RIGHT_HIP, LEFT_KNEE, 90, 120, 0),
           (RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE, 30, 75, 0),
           (LEFT_SHOULDER, LEFT_ELBOW, LEFT_WRIST, 140, 180, 1),
           (LEFT_ELBOW, LEFT_SHOULDER, LEFT_HIP, 140, 180, 1),
           (RIGHT_ELBOW, RIGHT_SHOULDER, RIGHT_HIP, 140, 180, 0),
           (RIGHT_SHOULDER, RIGHT_ELBOW, RIGHT_WRIST, 140, 180, 0)]

warrior_r = [(LEFT_HIP, LEFT_KNEE, LEFT_ANKLE, 30, 75, 1),
             (RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE,120, 180, 0),
           (LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE, 90, 120, 1),
           (RIGHT_SHOULDER, RIGHT_HIP, LEFT_KNEE, 90, 120, 0),
           (LEFT_SHOULDER, LEFT_ELBOW, LEFT_WRIST, 140, 180, 1),
           (LEFT_ELBOW, LEFT_SHOULDER, LEFT_HIP, 140, 180, 1),
           (RIGHT_ELBOW, RIGHT_SHOULDER, RIGHT_HIP, 140, 180, 0),
           (RIGHT_SHOULDER, RIGHT_ELBOW, RIGHT_WRIST, 140, 180, 0)]

PRINT_PARTS =[LEFT_SHOULDER,RIGHT_SHOULDER,LEFT_ELBOW,RIGHT_ELBOW,
              LEFT_WRIST,RIGHT_WRIST,LEFT_HIP,RIGHT_HIP,
              LEFT_KNEE,RIGHT_KNEE,LEFT_ANKLE,RIGHT_ANKLE]

