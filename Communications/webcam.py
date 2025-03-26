# IP address of Ben's pi: 192.168.0.103
import cv2
from flask import Flask, Response

app = Flask(__name__)
cam = cv2.VideoCapture(0,cv2.CAP_V4L2)


def generate_frames():
    while True:
        result, image = cam.read()
        ret, buffer = cv2.imencode('.jpg', image)
        image = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

