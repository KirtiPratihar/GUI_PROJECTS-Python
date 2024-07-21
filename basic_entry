from tkinter import *
from PIL import Image, ImageTk

root = Tk()
#gui logic
#root.geometry("700x700")
root.minsize(700,500)
txt=Label(text="Hi my name is Kirti Pratihar")
txt.pack()
#to insert a photo
#process-1
#photo = PhotoImage(file="51.png")
#Label = Label(image=photo)
#Label.pack()

#process-2
image=Image.open("51.png")
photo= ImageTk.PhotoImage(image)
Label = Label(image=photo)
Label.pack()

root.mainloop()

