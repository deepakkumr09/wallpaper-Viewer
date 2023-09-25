from tkinter import*
from PIL import ImageTk, Image
import os

def rotate_image():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter = counter + 1


counter =1
root = Tk()
root.title('Wallpaper Viewer By Deepak Kumar')

root.geometry('500x700')
root.configure(background='black')

files = os.listdir('Wallpapers')

img_array =[]
for file in files:
    img = Image.open(os.path.join('Wallpapers',file))
    resized_img = img.resize((400,500))
    img_array.append(ImageTk.PhotoImage(resized_img))
 

img_label = Label(root,image = img_array[0])
img_label.pack(pady=(15,10))

next_btn = Button(root,text = 'Next',bg='white',fg='black',width=38,height=2 ,command=rotate_image)
next_btn.pack()




root.mainloop()