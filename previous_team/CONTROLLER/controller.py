import cv2
import numpy as np
from tkinter import*
from PIL import Image, ImageTk
import time

# Defined Variables
prefix = "[Controller]"
window = Tk()
driveMotors = True
looping = None
keypressLoop = None
currentArmMotor = 1

#--------------------------------------------------------------------------------------------------------------
# Functions

# Get Current Time
def currentTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #return time.strftime("%m-%d-%Y %H:%M:%S", time.localtime())

# Debug Date/Time Function
def clock():
    time = currentTime()
    debug_dateTime.config(text = (" Date/Time:   " + time))
    window.after(1000, clock)

# Switch Function (Drive Motor/Arm Motor)
def switch():
    global driveMotors
    print("------------------------------------------------------------")
    if driveMotors:
        DriveToggle.config(image = armImage)
        debug_motorMode.config(text = " Current Mode:  [Arm]")
        driveMotors = False
        print(currentTime(), prefix, "Switched to Arm Motors")
        '''
        b0["state"] = "normal"
        b1["state"] = "normal"
        b2["state"] = "normal"
        b3["state"] = "normal"
        b4["state"] = "normal"
        b5["state"] = "normal"
        b6["state"] = "normal"
        b7["state"] = "normal"
        b8["state"] = "normal"
        b9["state"] = "normal"
        b10["state"] = "normal"
        b11["state"] = "normal"
        b12["state"] = "disabled"
        b13["state"] = "disabled"
        b14["state"] = "disabled"
        b15["state"] = "disabled"
        '''
    else:
        DriveToggle.config(image = driveImage)
        debug_motorMode.config(text = " Current Mode:  [Drive]")
        driveMotors = True
        print(currentTime(), prefix, "Switched to Drive Motors")
        '''
        b0["state"] = "disabled"
        b1["state"] = "disabled"
        b2["state"] = "disabled"
        b3["state"] = "disabled"
        b4["state"] = "disabled"
        b5["state"] = "disabled"
        b6["state"] = "disabled"
        b7["state"] = "disabled"
        b8["state"] = "disabled"
        b9["state"] = "disabled"
        b10["state"] = "disabled"
        b11["state"] = "disabled"
        b12["state"] = "normal"
        b13["state"] = "normal"
        b14["state"] = "normal"
        b15["state"] = "normal"
        '''

# Drive Motor Movement Functions
def start_DriveMotor(direction):
    global driveMotors
    if driveMotors:
        if direction == "forward":
            print(currentTime(), prefix, "Drive Motor: Move Forward...")
        if direction == "backward":
            print(currentTime(), prefix, "Drive Motor: Move Backward...")
        if direction == "left":
            print(currentTime(), prefix, "Drive Motor: Move Left...")
        if direction == "right":
            print(currentTime(), prefix, "Drive Motor: Move Right...")
        move(direction)
    else:
        print("[Error] Drive Motors are currently off")

def stop_DriveMotor(event):
    global looping
    global driveMotors
    if driveMotors:
        window.after_cancel(looping)
        looping = None
        print("Drive Motor: Stopping Motor...")

def move(direction):
    global looping
    if direction == "forward":
        print("*forward*")
    if direction == "backward":
        print("*backward*")
    if direction == "left":
        print("*left*")
    if direction == "right":
        print("*right*")
    looping = window.after(200, move, direction) #1000 ticks = 1 second

# Arm Motor Movement Functions
def start_ArmMotor(direction, motor):
    global driveMotors
    if not driveMotors:
        if direction == "forward":
            print(currentTime(), prefix, "Arm Motor [%d]: Move Forward" % motor)
        if direction == "backward":
            print(currentTime(), prefix, "Arm Motor [%d]: Move Backward" % motor)
        arm_move(direction, motor)
    else:
        print("[Error] Arm Motors are currently off")

def stop_ArmMotor(event):
    global looping
    global driveMotors
    if not driveMotors:
        window.after_cancel(looping)
        looping = None
        print("Arm Motor: Stopping Motor...")

def arm_move(direction, motor):
    global looping
    if direction == "forward":
        if motor == 1:
            print("*arm motor %d forward*" % motor)
        if motor == 2:
            print("*arm motor %d forward*" % motor)
        if motor == 3:
            print("*arm motor %d forward*" % motor)
        if motor == 4:
            print("*arm motor %d forward*" % motor)
        if motor == 5:
            print("*arm motor %d forward*" % motor)
        if motor == 6:
            print("*arm motor %d forward*" % motor)
    if direction == "backward":
        if motor == 1:
            print("*arm motor %d backward*" % motor)
        if motor == 2:
            print("*arm motor %d backward*" % motor)
        if motor == 3:
            print("*arm motor %d backward*" % motor)
        if motor == 4:
            print("*arm motor %d backward*" % motor)
        if motor == 5:
            print("*arm motor %d backward*" % motor)
        if motor == 6:
            print("*arm motor %d backward*" % motor)
    looping = window.after(200, arm_move, direction, motor) #1000 ticks = 1 second

def keypress_start_Motor(direction):
    global driveMotors
    global keypressLoop
    global currentArmMotor
    if driveMotors:
        if not keypressLoop:
            keypressLoop = True
            if direction == "forward":
                print(currentTime(), prefix, "Drive Motor: Move Forward...")
            if direction == "backward":
                print(currentTime(), prefix, "Drive Motor: Move Backward...")
            if direction == "left":
                print(currentTime(), prefix, "Drive Motor: Move Left...")
            if direction == "right":
                print(currentTime(), prefix, "Drive Motor: Move Right...")
            keypress_move(direction)
    else:
        if not keypressLoop:
            keypressLoop = True
            if direction == "forward":
                print(currentTime(), prefix, "Arm Motor [%d]: Move Forward" % currentArmMotor)
            if direction == "backward":
                print(currentTime(), prefix, "Arm Motor [%d]: Move Backward" % currentArmMotor)
            keypress_arm_move(direction)

def keypress_arm_move(direction):
    global keypressLoop
    global currentArmMotor
    if keypressLoop:
        if direction == "forward":
            if currentArmMotor == 1:
                print("*arm motor %d forward*" % currentArmMotor)
            if currentArmMotor == 2:
                print("*arm motor %d forward*" % currentArmMotor)
            if currentArmMotor == 3:
                print("*arm motor %d forward*" % currentArmMotor)
            if currentArmMotor == 4:
                print("*arm motor %d forward*" % currentArmMotor)
            if currentArmMotor == 5:
                print("*arm motor %d forward*" % currentArmMotor)
            if currentArmMotor == 6:
                print("*arm motor %d forward*" % currentArmMotor)
        if direction == "backward":
            if currentArmMotor == 1:
                print("*arm motor %d backward*" % currentArmMotor)
            if currentArmMotor == 2:
                print("*arm motor %d backward*" % currentArmMotor)
            if currentArmMotor == 3:
                print("*arm motor %d backward*" % currentArmMotor)
            if currentArmMotor == 4:
                print("*arm motor %d backward*" % currentArmMotor)
            if currentArmMotor == 5:
                print("*arm motor %d backward*" % currentArmMotor)
            if currentArmMotor == 6:
                print("*arm motor %d backward*" % currentArmMotor)
        window.after(200, keypress_arm_move, direction)

def keypress_move(direction):
    global keypressLoop
    if keypressLoop:
        if direction == "forward":
            print("*forward*")
        if direction == "backward":
            print("*backward*")
        if direction == "left":
            print("*left*")
        if direction == "right":
            print("*right*")
        window.after(200, keypress_move, direction)

def keypress_stop_Motor(direction):
    global driveMotors
    global keypressLoop
    keypressLoop = False
    if driveMotors:
        print("Drive Motor: Stopping Motor...")
    else:
        if direction == "forward" or direction == "backward":
            print("Arm Motor: Stopping Motor...")

def motorSwitch(motorNum):
    global currentArmMotor
    currentArmMotor = motorNum
    #debug_currentArmMotor.config(text = " Current Arm Motor:  [%d]" % currentArmMotor)
    if currentArmMotor == 1:
        debug_currentArmMotor.config(text = " Current Arm Motor:  [1]  2   3   4   5   6 ")
    if currentArmMotor == 2:
        debug_currentArmMotor.config(text = " Current Arm Motor:   1  [2]  3   4   5   6 ")
    if currentArmMotor == 3:
        debug_currentArmMotor.config(text = " Current Arm Motor:   1   2  [3]  4   5   6 ")
    if currentArmMotor == 4:
        debug_currentArmMotor.config(text = " Current Arm Motor:   1   2   3  [4]  5   6 ")
    if currentArmMotor == 5:
        debug_currentArmMotor.config(text = " Current Arm Motor:   1   2   3   4  [5]  6 ")
    if currentArmMotor == 6:
        debug_currentArmMotor.config(text = " Current Arm Motor:   1   2   3   4   5  [6]")

#--------------------------------------------------------------------------------------------------------------
# Window Properties
window.geometry("960x540")
window.configure(bg = "#ffffff")
window.title("Rover Controller")

# Window Keybinds
window.bind('<Escape>', lambda e: window.quit())
window.bind('<Tab>', lambda e: switch())

window.bind('<w>', lambda event, direction="forward": keypress_start_Motor(direction))
window.bind('<KeyRelease-w>', lambda event, direction="forward": keypress_stop_Motor(direction))
window.bind('<a>', lambda event, direction="left": keypress_start_Motor(direction))
window.bind('<KeyRelease-a>', lambda event, direction="left": keypress_stop_Motor(direction))
window.bind('<s>', lambda event, direction="backward": keypress_start_Motor(direction))
window.bind('<KeyRelease-s>', lambda event, direction="backward": keypress_stop_Motor(direction))
window.bind('<d>', lambda event, direction="right": keypress_start_Motor(direction))
window.bind('<KeyRelease-d>', lambda event, direction="right": keypress_stop_Motor(direction))

window.bind('<Up>', lambda event, direction="forward": keypress_start_Motor(direction))
window.bind('<KeyRelease-Up>', lambda event, direction="forward": keypress_stop_Motor(direction))
window.bind('<Left>', lambda event, direction="left": keypress_start_Motor(direction))
window.bind('<KeyRelease-Left>', lambda event, direction="left": keypress_stop_Motor(direction))
window.bind('<Down>', lambda event, direction="backward": keypress_start_Motor(direction))
window.bind('<KeyRelease-Down>', lambda event, direction="backward": keypress_stop_Motor(direction))
window.bind('<Right>', lambda event, direction="right": keypress_start_Motor(direction))
window.bind('<KeyRelease-Right>', lambda event, direction="right": keypress_stop_Motor(direction))

window.bind('1', lambda event, motorNum=1: motorSwitch(motorNum))
window.bind('2', lambda event, motorNum=2: motorSwitch(motorNum))
window.bind('3', lambda event, motorNum=3: motorSwitch(motorNum))
window.bind('4', lambda event, motorNum=4: motorSwitch(motorNum))
window.bind('5', lambda event, motorNum=5: motorSwitch(motorNum))
window.bind('6', lambda event, motorNum=6: motorSwitch(motorNum))

#--------------------------------------------------------------------------------------------------------------
# GUI Background
canvas = Canvas(window, bg = "#ffffff", height = 540, width = 960, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)
background_img = PhotoImage(file = f"images/background.png")
background = canvas.create_image(480.0, 270.0, image=background_img)

#--------------------------------------------------------------------------------------------------------------
# Arm Motor 6: Backward Button
img0 = PhotoImage(file = f"images/img0.png")
b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b0.place(x = 405, y = 436, width = 45, height = 67)
b0.bind('<ButtonPress-1>', lambda event, direction="backward", motor=6: start_ArmMotor(direction, motor))
b0.bind('<ButtonRelease-1>', stop_ArmMotor)

#--------------------------------------------------------------------------------------------------------------
# Arm Motor 6: Forward Button
img1 = PhotoImage(file = f"images/img1.png")
b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b1.place(x = 405, y = 365, width = 45, height = 67)
b1.bind('<ButtonPress-1>', lambda event, direction="forward", motor=6: start_ArmMotor(direction, motor))
b1.bind('<ButtonRelease-1>', stop_ArmMotor)

#--------------------------------------------------------------------------------------------------------------
# Arm Motor 5: Backward Button
img2 = PhotoImage(file = f"images/img2.png")
b2 = Button(image = img2, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b2.place(x = 333, y = 436, width = 45, height = 67)
b2.bind('<ButtonPress-1>', lambda event, direction="backward", motor=5: start_ArmMotor(direction, motor))
b2.bind('<ButtonRelease-1>', stop_ArmMotor)

#--------------------------------------------------------------------------------------------------------------
# Arm Motor 5: Forward Button
img3 = PhotoImage(file = f"images/img3.png")
b3 = Button(image = img3, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b3.place(x = 333, y = 365, width = 45, height = 67)
b3.bind('<ButtonPress-1>', lambda event, direction="forward", motor=5: start_ArmMotor(direction, motor))
b3.bind('<ButtonRelease-1>', stop_ArmMotor)

#--------------------------------------------------------------------------------------------------------------
# Arm Motor 4: Backward Button
img4 = PhotoImage(file = f"images/img4.png")
b4 = Button(image = img4, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b4.place(x = 262, y = 436, width = 45, height = 67)
b4.bind('<ButtonPress-1>', lambda event, direction="backward", motor=4: start_ArmMotor(direction, motor))
b4.bind('<ButtonRelease-1>', stop_ArmMotor)

#--------------------------------------------------------------------------------------------------------------
# Arm Motor 4: Forward Button
img5 = PhotoImage(file = f"images/img5.png")
b5 = Button(image = img5, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b5.place(x = 262, y = 365, width = 45, height = 67)
b5.bind('<ButtonPress-1>', lambda event, direction="forward", motor=4: start_ArmMotor(direction, motor))
b5.bind('<ButtonRelease-1>', stop_ArmMotor)

#--------------------------------------------------------------------------------------------------------------
# Arm Motor 3: Backward Button
img6 = PhotoImage(file = f"images/img6.png")
b6 = Button(image = img6, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b6.place(x = 191, y = 436, width = 45, height = 67)
b6.bind('<ButtonPress-1>', lambda event, direction="backward", motor=3: start_ArmMotor(direction, motor))
b6.bind('<ButtonRelease-1>', stop_ArmMotor)

#--------------------------------------------------------------------------------------------------------------
# Arm Motor 3: Forward Button
img7 = PhotoImage(file = f"images/img7.png")
b7 = Button(image = img7, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b7.place(x = 191, y = 365, width = 45, height = 67)
b7.bind('<ButtonPress-1>', lambda event, direction="forward", motor=3: start_ArmMotor(direction, motor))
b7.bind('<ButtonRelease-1>', stop_ArmMotor)

#--------------------------------------------------------------------------------------------------------------
# Arm Motor 2: Backward Button
img8 = PhotoImage(file = f"images/img8.png")
b8 = Button(image = img8, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b8.place(x = 120, y = 436, width = 45, height = 67)
b8.bind('<ButtonPress-1>', lambda event, direction="backward", motor=2: start_ArmMotor(direction, motor))
b8.bind('<ButtonRelease-1>', stop_ArmMotor)

#--------------------------------------------------------------------------------------------------------------
# Arm Motor 2: Forward Button
img9 = PhotoImage(file = f"images/img9.png")
b9 = Button(image = img9, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b9.place(x = 120, y = 365, width = 45, height = 67)
b9.bind('<ButtonPress-1>', lambda event, direction="forward", motor=2: start_ArmMotor(direction, motor))
b9.bind('<ButtonRelease-1>', stop_ArmMotor)

#--------------------------------------------------------------------------------------------------------------
# Arm Motor 1: Backward Button
img10 = PhotoImage(file = f"images/img10.png")
b10 = Button(image = img10, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b10.place(x = 48, y = 436, width = 45, height = 67)
b10.bind('<ButtonPress-1>', lambda event, direction="backward", motor=1: start_ArmMotor(direction, motor))
b10.bind('<ButtonRelease-1>', stop_ArmMotor)

#--------------------------------------------------------------------------------------------------------------
# Arm Motor 1: Forward Button
img11 = PhotoImage(file = f"images/img11.png")
b11 = Button(image = img11, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b11.place(x = 48, y = 365, width = 45, height = 67)
b11.bind('<ButtonPress-1>', lambda event, direction="forward", motor=1: start_ArmMotor(direction, motor))
b11.bind('<ButtonRelease-1>', stop_ArmMotor)

#--------------------------------------------------------------------------------------------------------------
# Drive Motor: Right Button
img12 = PhotoImage(file = f"images/img12.png")
b12 = Button(image = img12, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b12.place(x = 831, y = 412, width = 45, height = 45)
b12.bind('<ButtonPress-1>', lambda event, direction="right": start_DriveMotor(direction))
b12.bind('<ButtonRelease-1>', stop_DriveMotor)

#--------------------------------------------------------------------------------------------------------------
# Drive Motor: Left Button
img13 = PhotoImage(file = f"images/img13.png")
b13 = Button(image = img13, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b13.place(x = 726, y = 412, width = 45, height = 45)
b13.bind('<ButtonPress-1>', lambda event, direction="left": start_DriveMotor(direction))
b13.bind('<ButtonRelease-1>', stop_DriveMotor)

#--------------------------------------------------------------------------------------------------------------
# Drive Motor: Backward Button
img14 = PhotoImage(file = f"images/img14.png")
b14 = Button(image = img14, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b14.place(x = 778, y = 465, width = 45, height = 45)
b14.bind('<ButtonPress-1>', lambda event, direction="backward": start_DriveMotor(direction))
b14.bind('<ButtonRelease-1>', stop_DriveMotor)

#--------------------------------------------------------------------------------------------------------------
# Drive Motor: Forward Button
img15 = PhotoImage(file = f"images/img15.png")
b15 = Button(image = img15, borderwidth = 0, highlightthickness = 0, command = None, relief = "flat")
b15.place(x = 778, y = 360, width = 45, height = 45)
b15.bind('<ButtonPress-1>', lambda event, direction="forward": start_DriveMotor(direction))
b15.bind('<ButtonRelease-1>', stop_DriveMotor)

#--------------------------------------------------------------------------------------------------------------
# Drive/Arm Toggle Switch
armImage = PhotoImage(file = f"images/img16.png")
driveImage = PhotoImage(file = f"images/img17.png")
DriveToggle = Button(image = driveImage, borderwidth = 0, highlightthickness = 0, command = switch, relief = "flat")
DriveToggle.place(x = 547, y = 139, width = 86, height = 30)

#--------------------------------------------------------------------------------------------------------------
# Debug Date/Time Text
debug_dateTime = Label(window, fg='white', bg='#2d2e32')
debug_dateTime.place(x=716, y=46)

#Debug Motor Mode Text
debug_motorMode = Label(window, text=" Current Mode:  [Drive]", fg='white', bg='#2d2e32')
debug_motorMode.place(x=716, y=63)

#Debug Motor Mode Text
debug_currentArmMotor = Label(window, text=" Current Arm Motor:  [1]  2   3   4   5   6 ", fg='white', bg='#2d2e32')
debug_currentArmMotor.place(x=716, y=80)

#--------------------------------------------------------------------------------------------------------------
# Camera View

frame_1 = Frame(window).place(x=0, y=0)
cap = cv2.VideoCapture(0)
#placement is off by 2 pixels
label1 = Label(frame_1, width=480, height=270)
label1.place(x=13, y=13)
#label2 = Label(frame_1, width=192, height=108)
#label2.place(x=508, y=13)
#label3 = Label(frame_1, width=259, height=146)
#label3.place(x=684.25, y=137.5)

def camera():
    _,img = cap.read()
    #_,img2 = cap.read()
    #_,img3 = cap.read()

    img = cv2.flip(img, 1)
    img = cv2.resize(img, (480, 270))
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #img2 = cv2.flip(img2, 1)
    #img2 = cv2.resize(img2, (192, 108))
    #rgb2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    #img3 = cv2.flip(img3, 1)
    #img3 = cv2.resize(img3, (259, 146))
    #rgb3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

    image = Image.fromarray(rgb)
    iago = ImageTk.PhotoImage(image)
    label1.configure(image=iago)
    label1.image = iago

    #image_2 = Image.fromarray(rgb2)
    #iago_2 = ImageTk.PhotoImage(image_2)
    #label2.configure(image=iago_2)
    #label2.image = iago_2

    #image_3 = Image.fromarray(rgb3)
    #iago_3 = ImageTk.PhotoImage(image_3)
    #label3.configure(image=iago_3)
    #label3.image = iago_3

    window.after(2, camera)

#--------------------------------------------------------------------------------------------------------------

clock()
camera()
window.resizable(False, False)
window.mainloop()