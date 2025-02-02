from tkinter import *

root = Tk()

def my_mainloop():
    print("Hello World!")
    root.after(1000, my_mainloop)    

root.after(0, my_mainloop)
root.mainloop()