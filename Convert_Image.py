from tkinter import*
from tkinter import Tk, ttk

from PIL import Image, ImageTk
from tkinter import filedialog as fd

import cv2

co0 = "#ffffff"
co1 = "#000000"
co2 = "#63b9ff"

window = Tk ()
window.title("")
window.geometry('378x350')
window.configure(background=co0)
window.resizable(width=FALSE, height=FALSE)

global original_img, l_img, img

original_img = ['']

def choose_img():
    global original_img, l_img, img

    img = fd.askopenfilename()
    print(img)
    original_img.append(img)

    img = Image.open(img)
    img = img.resize((200, 150))
    img = ImageTk.PhotoImage(img)

    l_img = Label(window, image = img, bg = co0, fg=co1)
    l_img.place(x=60, y=60)

def converted_img():
    global original_img, l_img, img

    scale_value = scale.get()

# load the choosen image

    img = cv2.imread(original_img[-1])

# convert one colorspace to another
    converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred_img = cv2.GaussianBlur(converted_img, (25, 25), 300, 300)

    img_to_pencil = cv2.divide(converted_img, blurred_img, scale = scale_value)

    cv2.imwrite('saved_img.png', img_to_pencil)

    img = Image.open('saved_img.png')
    img = img.resize((110, 200))
    img = ImageTk.PhotoImage(img)

    l_img = Label(window, image = img, bg = co0, fg=co1)
    l_img.place(x=60, y=60)


style = ttk.Style(window)
style.theme_use("clam")

app_img = Image.open("logo.png")
app_img = app_img.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(window, image=app_img, text="img to > pencil sketch", width=300, compound=LEFT, relief=RAISED, anchor=NW, font=('System 15 bold'), bg=co0, fg=co1)
app_logo.place(x=0, y=0)

l_options = Label(window, text = "Settings --------------------------------------------------".upper(), anchor=NW, font=('verdana 7 bold'), bg=co0, fg=co1)
l_options.place(x=10, y=260)

scale = Scale(window, from_=0, to=255, length = 120, bg=co0, fg='red', orient=HORIZONTAL)
scale.place(x=10, y=300)

b_choose = Button(window, text= "Choose img", command = choose_img, width=15, overrelief=RIDGE, font=('Ivy 10'), bg=co2, fg=co1)
b_choose.place(x=147, y=287)

b_save = Button(window, text= "Save img", command=converted_img, width=15, overrelief=RIDGE, font=('Ivy 10'), bg=co2, fg=co1)
b_save.place(x=147, y=317)


window.mainloop()