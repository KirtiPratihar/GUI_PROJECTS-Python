from tkinter import *
from  PIL import Image , ImageTk
root = Tk()

#root.geometry("400x600")
root.title("Important topic to remind")
root.minsize(1000,400)
#important Label Options
#text - adds the text
#bd - background
#fg - foreground
#font - sets the fonts
#font=("comicsans",15,"bold")
#padx - x padding
#pady - y padding
#relief - border styling - SUNKEN, RAISED, GROOVE,RIDGE



title_label = Label(text='''A computer might be described with deceptive simplicity as “an apparatus that performs routine calculations automatically.”
 Such a definition would owe its deceptiveness to a naive and narrow
view of calculation as a strictly mathematical process. In fact, \n calculation underlies many activities that are not normally thought of as mathematical. Walking across a room, for instance,
requires many complex, albeit subconscious, calculations. Computers, too, have proved capable of solving a vast array of problems0,\n from balancing a checkbook to even—in the form of 
guidance systems for robots—walking across a room.''',bg="violet",fg="white"
                    ,padx=23, pady=24,font= "oswald 10 bold",borderwidth=3,relief="groove")

#title_label.pack(anchor= "nw")
title_label.pack(side= "top",anchor= "ne")

#IMPORTENT PACK OPTION
#anchor= "nw"
#side= top,bottom,left,right
#so for makinf the box on the down left corner-
#title_label.pack(side= "bottom",anchor= "nw")
#fill=x     - uses for x line
root.mainloop()
