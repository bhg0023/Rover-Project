# Written By: Benjamin Goldberg
# 2025
#
#
# This code will open the webcam as a video capture device in opencv, 
# and take frames a jpeg. 
# 
# As of right now, a flask server is created to be able to moniter the
# webcam feed in the browser.


# type: "http://<IP ADDRESS OF PI>:5000/video_feed" into your web browser to view


import cv2
from flask import Flask, Response
import time

app = Flask(__name__)
cam = cv2.VideoCapture(0,cv2.CAP_V4L2)  #pipline set to CAP_V4L2 to avoid pipeline error


def generate_frames():
    while True:
        result, image = cam.read()
        ret, buffer = cv2.imencode('.jpg', image)
        image = buffer.tobytes()
        return image
        # yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')
    




""" for i in range (0, 1):
    out = generate_frames()
    print(out)
    time.sleep(0.001)


print("End of webcam read") """

""" @app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 """

