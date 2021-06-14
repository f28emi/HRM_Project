from tkinter import *

root=Tk()

firstmenu=Menu(root)
root.config(menu=firstmenu)

frame=Frame(root)
frame.pack()

def fun1():
    print("New Project Clicked")

def fun2():
    print("New Clicked")

def fun3():
    print("New Scratch File Clicked")

def fun4():
    print("Open Clicked")

def fun5():
    print("Save As Clicked")

def fun6():
    print("Appearance Clicked")

def fun7():
    print("Undo Typing Clicked")


def fun8():
    print("Redo Clicked")


def fun9():
    print("Cut Clicked")


def fun10():
    print("Copy Clicked")


def fun11():
    print("Paste Clicked")


def fun12():
    print("Delete Clicked")


def fun13():
    print("Tool Windows Clicked")


def fun14():
    print("Quick Definition Clicked")


def fun15():
    print("Quick Type Definition Clicked")


def fun16():
    print("Quick Documentation Clicked")


def fun17():
    print("Parameter Info Clicked")


def fun18():
    print("Back Clicked")

def fun19():
    print("Forward Clicked")


def fun20():
    print("Search Everywhere Clicked")


def fun21():
    print("Class... Clicked")


def fun22():
    print("File... Clicked")


def fun23():
    print("Symbol... Clicked")


def fun24():
    print("Override Methods... Clicked")


def fun25():
    print("Implement Methods... Clicked")


def fun26():
    print("Generate... Clicked")


def fun27():
    print("Code Completion Clicked")


def fun28():
    print("Insert Live Template... Clicked")

def fun29():
    print("Surround With... Clicked")


firstsub=Menu(firstmenu)
firstmenu.add_cascade(label="File",menu=firstsub)
firstsub.add_command(label="New Project...",command=fun1)
firstsub.add_command(label="New",command=fun2)
firstsub.add_separator()
firstsub.add_command(label="New Scratch File",command=fun3)
firstsub.add_command(label="Open",command=fun4)
firstsub.add_separator()
firstsub.add_command(label="Save As",command=fun5)
firstsub.add_command(label="Exit",command=frame.quit)
firstsub.add_separator()

secondmenu=Menu(firstmenu)
firstmenu.add_cascade(label="Edit",menu=secondmenu)
secondmenu.add_command(label="Undo Typing",command=fun7)
secondmenu.add_command(label="Redo",command=fun8)
secondmenu.add_separator()
secondmenu.add_command(label="Cut",command=fun9)
secondmenu.add_command(label="Copy",command=fun10)
secondmenu.add_separator()
secondmenu.add_command(label="Paste",command=fun11)
secondmenu.add_command(label="Delete",command=fun12)
secondmenu.add_separator()


thirdmenu=Menu(firstmenu)
firstmenu.add_cascade(label="View",menu=thirdmenu)
thirdmenu.add_command(label="Tool Windows",command=fun13)
thirdmenu.add_command(label="Appearance",command=fun6)
thirdmenu.add_separator()
thirdmenu.add_command(label="Quick Definition",command=fun14)
thirdmenu.add_command(label="Quick Type Definition",command=fun15)
thirdmenu.add_separator()
thirdmenu.add_command(label="Quick Documentation",command=fun16)
thirdmenu.add_command(label="Parameter Info",command=fun17)
thirdmenu.add_separator()


fourthmenu=Menu(firstmenu)
firstmenu.add_cascade(label="Navigate",menu=fourthmenu)
fourthmenu.add_command(label="Back",command=fun18)
fourthmenu.add_command(label="Forward",command=fun19)
fourthmenu.add_separator()
fourthmenu.add_command(label="Search Everywhere",command=fun20)
fourthmenu.add_command(label="Class...",command=fun21)
fourthmenu.add_separator()
fourthmenu.add_command(label="File...",command=fun22)
fourthmenu.add_command(label="Symbol...",command=fun23)
fourthmenu.add_separator()


fifthmenu=Menu(firstmenu)
firstmenu.add_cascade(label="Code",menu=fifthmenu)
fifthmenu.add_command(label="Override Methods...",command=fun24)
fifthmenu.add_command(label="Implement Methods...",command=fun25)
fifthmenu.add_separator()
fifthmenu.add_command(label="Generate...",command=fun26)
fifthmenu.add_command(label="Code Completion",command=fun27)
fifthmenu.add_separator()
fifthmenu.add_command(label="Insert Live Template...",command=fun28)
fifthmenu.add_command(label="Surround With...",command=fun29)
fifthmenu.add_separator()

root.mainloop()