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

body_part = {
0:'nose',
1:'left eye inner',
2:'left eye',
3:'left eye outer',
4:'right eye inner',
5:'right eye',
6:'right eye outer',
7:'left ear',
8:'right ear',
9:'mouth left',
10:'mouth right',
11:'left shoulder',
12:'right shoulder',
13:'left elbow',
14:'right elbow',
15:'left wrist',
16:'right wrist',
17:'left pinky',
18:'right pinky',
19:'left index',
20:'right index',
21:'left thumb',
22:'right thumb',
23:'left hip',
24:'right hip',
25:'left knee',
26:'right knee',
27:'left ankle',
28:'right ankle',
29:'left heel',
30:'right heel',
31:'left foot index',
32:'right foot index'
}

### Colors
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

### Positions
warrior = [(LEFT_HIP, LEFT_KNEE, LEFT_ANKLE, 120, 180, 1),
           (LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE, 90, 120, 1),
           (RIGHT_SHOULDER, RIGHT_HIP, LEFT_KNEE, 90, 120, 0),
           (RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE, 30, 75, 0),
           (LEFT_SHOULDER, LEFT_ELBOW, LEFT_WRIST, 140, 180, 1),
           (LEFT_ELBOW, LEFT_SHOULDER, LEFT_HIP, 140, 180, 1),
           #(RIGHT_ELBOW, RIGHT_SHOULDER, RIGHT_HIP, 140, 180, 0),
           #(RIGHT_SHOULDER, RIGHT_ELBOW, RIGHT_WRIST, 140, 180, 0)
             ]


warrior3 = [(LEFT_HIP, LEFT_KNEE, LEFT_ANKLE, 120, 180, 1),
           (LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE, 90, 120, 1),
           (RIGHT_SHOULDER, RIGHT_HIP, LEFT_KNEE, 90, 120, 0),
           (RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE, 160, 180, 0),
           (LEFT_SHOULDER, LEFT_ELBOW, LEFT_WRIST, 30, 75, 1),
           (LEFT_ELBOW, LEFT_SHOULDER, LEFT_HIP, 0, 30, 1),
           #(RIGHT_ELBOW, RIGHT_SHOULDER, RIGHT_HIP, 0, 30, 0),
           #(RIGHT_SHOULDER, RIGHT_ELBOW, RIGHT_WRIST, 30, 75, 0)
              ]



dog = [(LEFT_HIP, LEFT_KNEE, LEFT_ANKLE, 120, 180, 1),
           (LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE, 80, 110, 1),
           # (RIGHT_SHOULDER, RIGHT_HIP, LEFT_KNEE, 80, 110, 0),
           # (RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE, 160, 180, 0),
           (LEFT_SHOULDER, LEFT_ELBOW, LEFT_WRIST, 140, 180, 1),
           (LEFT_ELBOW, LEFT_SHOULDER, LEFT_HIP, 140, 180, 1),
           # (RIGHT_ELBOW, RIGHT_SHOULDER, RIGHT_HIP, 140, 180, 0),
           # (RIGHT_SHOULDER, RIGHT_ELBOW, RIGHT_WRIST, 140, 180, 0)
          ]

pillow = [(LEFT_HIP, LEFT_KNEE, LEFT_ANKLE, 120, 180, 1),
            (LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE, 30, 75, 1),
            # (RIGHT_SHOULDER, RIGHT_HIP, LEFT_KNEE, 30, 75, 0),
            # (RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE, 120, 180, 0),
            (LEFT_SHOULDER, LEFT_ELBOW, LEFT_WRIST, 70, 120, 1),
            (LEFT_ELBOW, LEFT_SHOULDER, LEFT_HIP, 30, 100, 1),
            # (RIGHT_ELBOW, RIGHT_SHOULDER, RIGHT_HIP, 30, 100, 0),
            # (RIGHT_SHOULDER, RIGHT_ELBOW, RIGHT_WRIST, 70, 120, 0)
            ]

dance = [(LEFT_HIP, LEFT_KNEE, LEFT_ANKLE, 30,90, 1),
           (LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE, 70, 110, 1),
            # (RIGHT_SHOULDER, RIGHT_HIP, LEFT_KNEE, 70, 110, 0),
           (RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE, 160, 180, 0),
           (LEFT_SHOULDER, LEFT_ELBOW, LEFT_WRIST, 30, 150, 1),
           (LEFT_ELBOW, LEFT_SHOULDER, LEFT_HIP, 90, 150, 1),
           # (RIGHT_ELBOW, RIGHT_SHOULDER, RIGHT_HIP, 90, 150, 0),
           # (RIGHT_SHOULDER, RIGHT_ELBOW, RIGHT_WRIST, 100, 150, 0)
           ]

twolegs = [(LEFT_HIP, LEFT_KNEE, LEFT_ANKLE, 100,140, 1),
            (LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE, 100,140, 1),
            #(RIGHT_SHOULDER, RIGHT_HIP, LEFT_KNEE, 100,140, 0),
            #(RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE, 100,140, 0),
            (LEFT_SHOULDER, LEFT_ELBOW, LEFT_WRIST, 30, 100, 1),
            (LEFT_ELBOW, LEFT_SHOULDER, LEFT_HIP, 100,160, 1),
            #(RIGHT_ELBOW, RIGHT_SHOULDER, RIGHT_HIP, 100,160, 0),
            #(RIGHT_SHOULDER, RIGHT_ELBOW, RIGHT_WRIST, 30, 100, 0)
             ]

PRINT_PARTS =[LEFT_SHOULDER, LEFT_ELBOW, LEFT_HIP, LEFT_KNEE]

info_parts = {
    'warrior I.mp4':[LEFT_KNEE, LEFT_HIP, RIGHT_HIP, RIGHT_KNEE, LEFT_ELBOW, LEFT_SHOULDER],
    'warrior III.mp4':[LEFT_KNEE, LEFT_HIP, RIGHT_HIP, RIGHT_KNEE, LEFT_ELBOW, LEFT_SHOULDER],
    'downward-dog.mp4':[LEFT_KNEE, LEFT_HIP, LEFT_ELBOW, LEFT_SHOULDER],
    'warrior II.mp4':[LEFT_KNEE, LEFT_HIP, LEFT_ELBOW, LEFT_SHOULDER],
    'wheel pose.mp4':[LEFT_KNEE, LEFT_HIP, RIGHT_KNEE, LEFT_ELBOW, LEFT_SHOULDER],
    'bridge.mp4':[LEFT_KNEE, LEFT_HIP, LEFT_ELBOW, LEFT_SHOULDER]
}

positions_id = {
    'warrior I.mp4':warrior,
    'warrior III.mp4':warrior3,
    'downward-dog.mp4':dog,
    'warrior II.mp4':pillow,
    'wheel pose.mp4':dance,
    'bridge.mp4':twolegs
}
