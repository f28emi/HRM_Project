from tkinter import *
from PIL import ImageTk,Image
import pyqrcode
root=Tk()

def generate():
    link_name=name_Entry.get()
    link=link_Entry.get()
    file_name=link_name+".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,230,window=image_label)

canvas=Canvas(root,width=400,height=600)
canvas.pack()
app_label=Label(root,text="QR Code Generator",fg="Blue",font=("Arial",30))
canvas.create_window(200,50,window=app_label)
name_label=Label(root,text='Link Name')
link_label=Label(root,text='Link')

name_Entry=Entry(root)
link_Entry=Entry(root)


canvas.create_window(200,100,window=name_label)
canvas.create_window(200,160,window=link_label)

name_Entry=Entry(root)
link_Entry=Entry(root)

canvas.create_window(200,130,window=name_Entry)
canvas.create_window(200,180,window=link_Entry)

button1=Button(text="Generate",command=generate)
canvas.create_window(200,230,window=button1)

root.mainloop()