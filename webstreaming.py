# import the necessary packages
from pose.Pose import PoseDetector
from pose.stats import *
from imutils.video import VideoStream
from flask import Response, request
from flask import Flask
from flask import render_template
import threading
import argparse
import imutils
import time
import cv2
import pyttsx3
id = 'warrior I.mp4'
position = warrior
# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
outputFrame = None
lock = threading.Lock()
# initialize a flask object
app = Flask(__name__,
            static_url_path='',
            static_folder='public')
# initialize the video stream and allow the camera sensor to
# warmup
#vs = VideoStream(usePiCamera=1).start()
vs = VideoStream(src=0).start()
time.sleep(2.0)
check = False
start = 0
elapsed =0
@app.route("/")
def index():
   global check
   check = False
   global start
   start = time.time()
   # return the rendered template
   return render_template("index.html")
@app.route("/yoga_pose")
def yoga_pose():
   global check
   check = False
   global start
   start = time.time()
   # return the rendered template
   return render_template("yoga_pose.html")

@app.route("/yoga_video")
def yoga_video():
   global check
   check = False
   global start
   start = time.time()
   global id
   id = request.args.get('id')
   global position
   position = positions_id[id]
   print(position)
   return render_template("yoga_video.html")

@app.route("/webcam")
def webcam():
   global check
   check = True
   # return the rendered template
   return render_template("webcam.html")

def detect_motion(frameCount):
   # grab global references to the video stream, output frame, and
   # lock variables
   global vs, outputFrame, lock
   global start
   start = time.time()
   while True:
      # read the next frame from the video stream, resize it,
      # convert the frame to grayscale, and blur it
      frame = vs.read()
      frame = imutils.resize(frame, width=640)
      global elapsed
      if check:
         elapsed = time.time() - start
         checking = elapsed
         print(elapsed)
         if checking > 10:
            if not all(x is None for x in detect.arrows):
               for i, move in enumerate(detect.arrows):
                  if move in [['↓'], ['↑'], ['←'], ['→']]:
                     synthesizer = pyttsx3.init()
                     synthesizer.say('Move your')
                     synthesizer.runAndWait()
                     synthesizer.stop()
                     number = info_parts[id][i]
                     body_name = body_part[number]
                     synthesizer.say(body_name)
                     synthesizer.runAndWait()
                     synthesizer.stop()
                     synthesizer.say(detect.speech[move[0]])
                     synthesizer.runAndWait()
                     synthesizer.stop()
            detect.arrows = []

            detect.first_time = True
         elapsed = 0
         frame = detect.findPose(frame)
         positions = detect.findPosition(frame)

         if len(positions) != 0:
            temps = []
            for angles in position:
               frame, temp = detect.calculate_angle(frame, positions, *angles)
               temps.append(temp)

            if detect.first_time:
               detect.arrows = temps
               detect.first_time = False
            else:
               for i, temp in enumerate(temps):
                  if detect.arrows[i] != temp:
                     detect.arrows[i] = None

      with lock:
         outputFrame = frame.copy()

def generate():
   # grab global references to the output frame and lock variables
   global outputFrame, lock
   # loop over frames from the output stream
   while True:
      # wait until the lock is acquired
      with lock:
         # check if the output frame is available, otherwise skip
         # the iteration of the loop
         if outputFrame is None:
            continue
         # encode the frame in JPEG format
         (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
         # ensure the frame was successfully encoded
         if not flag:
            continue
      # yield the output frame in the byte format
      yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
         bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
   global check
   check = True
   # return the response generated along with the specific media
   # type (mime type)
   return Response(generate(),
      mimetype = "multipart/x-mixed-replace; boundary=frame")

# check to see if this is the main thread of execution
if __name__ == '__main__':
   # construct the argument parser and parse command line arguments
   ap = argparse.ArgumentParser()
   ap.add_argument("-i", "--ip", type=str, required=True,
      help="ip address of the device")
   ap.add_argument("-o", "--port", type=int, required=True,
      help="ephemeral port number of the server (1024 to 65535)")
   ap.add_argument("-f", "--frame-count", type=int, default=32,
      help="# of frames used to construct the background model")
   args = vars(ap.parse_args())
   # start a thread that will perform motion detection
   detect = PoseDetector()
   t = threading.Thread(target=detect_motion, args=(
      args["frame_count"],))
   t.daemon = True
   t.start()
   # start the flask app
   app.run(host=args["ip"], port=args["port"], debug=True,
      threaded=True, use_reloader=False)
# release the video stream pointer
vs.stop()
