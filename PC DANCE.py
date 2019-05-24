from tkinter import *
from tkinter import ttk
import subprocess
import os                                                                       
 
window = Tk()
canvas = Canvas(window, width = 300, height = 300)      
canvas.pack( side = LEFT)      
img = PhotoImage(file="PCDANCE.png")      
canvas.create_image(20,20, anchor=NW, image=img)      
def DiskDrive():
    os.startfile("Keyboard.vbs")
def Keyboard():
    os.startfile("Keyboard.vbs")
    
def All():
    os.startfile("startboth.bat")
def Close():
    window.destroy()
def stopscripts():
    os.popen("taskkill /F /IM wscript.exe")
    
def about():
    window = Tk()
    window.title("PC Dance: About")
    Label1 = Label(window, text="PC Dance is a project to make the software and hardware of \n your computer  act like its dancing we currently have 2 options.\n First is a script that makes your keyboard lights flicker.\n Secondly a script that makes the disk drive open and shut constantly.")
    Label1.pack()
    window.mainloop()


    
button = ttk.Button(window, text="DISKDRIVE", command = DiskDrive)
button2 = ttk.Button(window, text="KEYBOARD", command = Keyboard)
button3 = ttk.Button(window, text="START ALL", command = All)
button4 = ttk.Button(window, text="ABOUT", command = about)
button5 = ttk.Button(window, text="STOP SCRIPTS", command = stopscripts)
button6 = ttk.Button(window, text="                        Close Window \n (Any running scripts will not be stoped)", command = All)

button.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()

window.title("PC DANCE")
window.resizable(False, False)
window.geometry("+300+300")
window.iconbitmap('favicon.ico')

window.mainloop()
