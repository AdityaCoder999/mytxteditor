import os
from tkinter import *
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename

def help1():
    msg.showinfo("About This Aditya Pad", "This will help you to open any text file. --> By AdityaCoder999")
def newFile():
    global file
    root.title("Untitled -  AdityaPad")
    file = None
    note.delete(1.0, END)
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - AdityaPad")
        note.delete(1.0, END)
        with open(file, "r") as f:
            note.insert(1.0, f.read())

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:
            with open(file, "w") as f:
                f.write(note.get(1.0, END))

            root.title(os.path.basename(file) + " - AdityaPad")

    else:
        with open(file, "w") as f:
                f.write(note.get(1.0, END))

def cut():
    note.event_generate(("<<Cut>>"))
def copy():
    note.event_generate(("<<Copy>>"))
def paste():
    note.event_generate(("<<Paste>>"))

root = Tk()
#our logic starts here --> 
root.geometry("1800x800")
root.title("Untitled - Adityapad")
root.wm_iconbitmap("icon.ico")

mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New File        ", command=newFile)
m1.add_command(label="Open File        ", command=openFile)
m1.add_command(label="Save        ", command=saveFile)
m1.add_separator()
m1.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)
m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut             ", command=cut)
m2.add_command(label="Copy             ", command=copy)
m2.add_command(label="Paste             ", command=paste)
root.config(menu=mainmenu)
m5 = Menu(mainmenu, tearoff=0)
m5.add_command(label="Help           ", command=help1)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="FILE", menu=m1)
mainmenu.add_cascade(label="EDIT", menu=m2)
mainmenu.add_cascade(label="HELP", menu=m5)

myscroll = Scrollbar(root)
myscroll.pack(side=RIGHT, fill=Y)
note = Text(root, yscrollcommand = myscroll.set, font="lucida 13")
file = None
note.pack(fill="both", expand=True)
myscroll.config(command = note.yview)

root.mainloop()