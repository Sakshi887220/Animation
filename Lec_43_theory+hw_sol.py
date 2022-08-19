from tkinter import *
import time
import random

root= Tk()
root.title("Moving objects")
root.geometry("800x800")

width, height = 600, 600

canvas = Canvas(root,width= width,height= height, bg='white')
canvas.pack(pady=20)


#code for theory lecture
"""
img=PhotoImage(file="snake.png")
img=img.subsample(5)
shape=canvas.create_image(100,100,image=img)

label=Label(root, text="")
label.pack(pady=20)

def pressed(event):
    global img
    img = PhotoImage(file="snake.png")
    img = img.subsample(5)
    canvas.create_image(event.x, event.y, image=img)

    label.config(text= "X: "+str(event.x) + " Y: "+ str(event.y))

root.bind("<B1-Motion>",pressed)

root.mainloop()
"""

#code for game

shape = canvas.create_oval(width/2,height/2,width/2+10,height/2+10,fill="red")
label=Label(root, text="")
label.pack(pady=20)


cx=width/2
cy=height/2
iter=0

def pressed(event):
    global cx
    global cy
    global iter
    global t1
    global t2
    global shape
    if abs(event.x - cx) <= 10 and abs(event.y - cy) <= 10:
        iter+=1
        cx=random.randrange(0,width-10)
        cy=random.randrange(0,height-10)
        choice=random.randrange(0,2)
        canvas.delete(shape)
        if choice == 1:
            shape=canvas.create_oval(cx, cy, cx + 10, cy + 10, fill="red")
        else:
            shape=canvas.create_rectangle(cx, cy, cx + 10, cy + 10, fill="red")

    if iter==1:
        t1=time.time()

    elif iter==20:
        t2=time.time()
        t=(t2-t1)
        t=round(t,3)
        text1 = "Time taken in previous round was: " + str(t) + " seconds"
        label.config(text= text1)
        iter=0


root.bind("<B1-Motion>",pressed)
root.mainloop()