#image editing app
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog

sameera = Tk()
sameera.geometry("1000x700")
sameera.bg="Blue"
sameera.title("Image editor")
#photo = PhotoImage(file="icon.ico.png")
image = Image.open("picture.jpg.jpg")
photo = ImageTk.PhotoImage(image)
image= image.resize((700,600))

def displayimage(image):
    dispimage=ImageTk.PhotoImage(image)
    sameera_label.configure(image=dispimage)
    sameera_label.image=dispimage

def rotate():
    global image
    image=image.rotate(90)
    displayimage(image)

def flip():
    global image
    image=image.transpose(Image.FLIP_LEFT_RIGHT)
    displayimage(image)

def opening():
    global image
    imagename= filedialog.askopenfilename(title="open")
    if imagename:
        image= Image.open(imagename)
        image= image.resize((600,600))
        displayimage(image)

def save():
    global image
    imagename =filedialog.asksaveasfilename(title="save",defaultextension=".jpg")
    if imagename:
        image.save(imagename)

sameera_label= Label(sameera,bg="BLACK")
sameera_label.grid(row=0,column=0,rowspan=12,padx=50,pady=50)
displayimage(image)

btnOpen= Button(sameera,text='Open',width=25,command=opening,bg="YELLOW")
btnOpen.grid(row=0,column=1)

btnRotate= Button(sameera,text='Rotate',width=25,command=rotate,bg="PINK")
btnRotate.grid(row=1,column=1)

btnFlip= Button(sameera,text='Flip',width=25,command=flip,bg="BLUE")
btnFlip.grid(row=2,column=1)

btnSave= Button(sameera,text='Save',width=25,command=save,bg="GREEN")
btnSave.grid(row=3,column=1)

#sameera_label.pack()
sameera.mainloop()