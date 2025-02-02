import cv2
import numpy as np
from tkinter import*
from PIL import Image, ImageTk

root = Tk()
root.title("Rover Controller")
root.geometry("670x600+200+30")
root.resizable(False, False)
w = 300
h = 200
color = "white"
#frame_1 = Frame(root, width=670, height=700, bg=color).place(x=0, y=0)
frame_1 = Frame(root, width=670, height=700).place(x=0, y=0)

cap = cv2.VideoCapture(0)

label1 = Label(frame_1, width=w, height=h)
label1.place(x=10, y=160)
label2 = Label(frame_1, width=w, height=h)
label2.place(x=350, y=160)

def camera():
    _,img = cap.read()
    img = cv2.resize(img, (w, h))
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    image = Image.fromarray(rgb)
    iago = ImageTk.PhotoImage(image)
    label1.configure(image=iago)
    label1.image = iago

    image_2 = Image.fromarray(rgb)
    iago_2 = ImageTk.PhotoImage(image_2)
    label2.configure(image=iago_2)
    label2.image = iago_2

    root.after(10, camera)

camera()
root.mainloop()