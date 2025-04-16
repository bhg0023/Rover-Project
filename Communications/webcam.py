# Written By: Benjamin Goldberg
# 2025
#
#
# This code will open the webcam as a video capture device in opencv, 
# and take frames a jpeg. 
# 



import cv2

cam = cv2.VideoCapture(0,cv2.CAP_V4L2)  #pipline set to CAP_V4L2 to avoid pipeline error


def generate_frames():
    while True:
        result, image = cam.read()
        ret, buffer = cv2.imencode('.jpg', image)
        image = buffer.tobytes()
        yield image
        # yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')
    
out = generate_frames()





