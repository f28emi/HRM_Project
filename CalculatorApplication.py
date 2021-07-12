from tkinter import *
root=Tk()
root.title("Calculator")

# creating drop down

#dropdown=Menu(root)
#root.config(menu=dropdown)


frame=Frame(root)
frame.grid()


#first=Menu(dropdown)
#dropdown.add_cascade(label="Menu",menu=first)
#first.add_command(label="Standard")
#first.add_command(label="Scientific")
#first.add_command(label="Graphing")
#first.add_command(label="Programmer")
#first.add_command(label="Date Calculation")
#first.add_separator()
#first.add_command(label="Currency")
#first.add_command(label="volume")
#first.add_command(label="Length")
#first.add_command(label="Area")
#first.add_command(label="Speed")
#first.add_command(label="Time")
#first.add_separator()
#first.add_command(label="About")


#second=Menu(dropdown)
#dropdown.add_cascade(label="Standard",menu=second)


#third=Menu(dropdown)
#dropdown.add_cascade(label="History",menu=third)

#fourth=Menu(dropdown)
#dropdown.add_cascade(label="Memory",menu=fourth)

# calc entry

textview=Entry(root)
textview.grid(row=1,columnspan=3000,sticky=E+W)















root.mainloop()