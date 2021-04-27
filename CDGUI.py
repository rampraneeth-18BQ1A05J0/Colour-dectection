import ColourDetection
from os.path import exists

try:
    import Tkinter as tk
    from Tkinter import messagebox
except ImportError:
    import tkinter as tk
    from tkinter import messagebox

#Global Variables
iname=""
def checkImage():
    #Function to check for the existance of the file
    if ImageEntry.get().strip() =='':
        return False
    p=ImageEntry.get()
    return bool(exists(p))
    
def destroy_window():
    # Function which closes the window.
    global top
    top.destroy()
    top= None

def startProcess():
    #Opening image
    if checkImage():
        ColourDetection.start(ImageEntry.get())
    else:
        messagebox.showerror('Error','Image Not Found')

top = tk.Tk()

top.geometry("600x450+670+251")
top.minsize(1, 1)
top.maxsize(1905, 1050)
top.resizable(1, 1)
top.title("Colour Detection - mini project")
top.configure(highlightcolor="black")

#Exit button
btnExit = tk.Button(top)
btnExit.place(relx=0.4, rely=0.778, height=29, width=129)
btnExit.configure(activebackground="#f9f9f9")
btnExit.configure(cursor="fleur")
btnExit.configure(text='''EXIT''')
btnExit.configure(command=destroy_window)

#Top label
Label1 = tk.Label(top)
Label1.place(relx=0.217, rely=0.2, height=59, width=348)
Label1.configure(highlightcolor="#1d18b5")
Label1.configure(text='''Enter Image Name with Complete Path''')

#Entry for image name
ImageEntry = tk.Entry(top)
ImageEntry.place(relx=0.15, rely=0.333,height=31, relwidth=0.677)
ImageEntry.configure(background="white")
ImageEntry.configure(font="TkFixedFont")
ImageEntry.configure(selectbackground="#c4c400")
ImageEntry.configure(textvariable=iname)

#Start button
startButton = tk.Button(top)
startButton.place(relx=0.25, rely=0.644, height=29, width=309)
startButton.configure(text='''Start Process''')
startButton.configure(command=startProcess)

#Heading
HeadingLabel = tk.Label(top)
HeadingLabel.place(relx=0.317, rely=0.067, height=56, width=204)
HeadingLabel.configure(background="#d9d9d9")
HeadingLabel.configure(foreground="#000000")
HeadingLabel.configure(font="-family {Conthrax} -size 14 -weight bold")
HeadingLabel.configure(relief="flat")
HeadingLabel.configure(justify='center')
HeadingLabel.configure(text='''Colour Detection''')

top.mainloop()
