from tkinter import *
from PIL import Image, ImageTk
import os

counter = 1
def rotate_image():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter += 1


root = Tk()

root.title("Wallpaper Viewer")
root.geometry('250x400')
root.config(bg="black")

files = os.listdir("c:\\Users\\shaba\\PycharmProjects\\Python-Problems\\tkinter\\wallpapers")

img_array = []
for file in files:
    img = Image.open(os.path.join("c:\\Users\\shaba\\PycharmProjects\\Python-Problems\\tkinter\\wallpapers", file))
    resized_img = img.resize((200,300))
    img = ImageTk.PhotoImage(resized_img)
    img_array.append(img)

img_label = Label(root, image= img_array[0])
img_label.pack(pady= (15,10))

nxt_btn = Button(root, text= "Next", bg= 'white', fg= 'black',width=28,height=2, command=rotate_image)
nxt_btn.pack()


root.mainloop()