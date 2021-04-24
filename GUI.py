import Enigma
import tkinter as tk
from tkinter import *
import sys
from PIL import ImageTk, Image

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='#404040')


def encrypt():
    inputMessage = plain_text.get()
    var1 = rotorSelection(self=True)
    rotorString = var1[0]
    reflector = var1[1]
    rotorStartPos = startLetter()
    rotorRingSetting = ringSetting()
    encryptedMessage = Enigma.encrypt(inputMessage, rotorString, rotorStartPos, "AC DS", reflector, rotorRingSetting)
    inputTextLabel.config(text=encryptedMessage)
    print(rotorStartPos)
    return encryptedMessage

def rotorSelection(self):

    rotor1 = str(clicked1.get())
    rotor2 = str(clicked2.get())
    rotor3 = str(clicked3.get())
    rotorPos = (rotor1+rotor2+rotor3)
    reflector = str(clickedRef.get())
    if len(rotorPos) >= 3:
        finalRotorPosition = rotorPos
        return finalRotorPosition, reflector

def startLetter():
    rotor1 = str(clicked4.get())
    rotor2 = str(clicked5.get())
    rotor3 = str(clicked6.get())
    startString = (rotor1+rotor2+rotor3)
    if len(startString) >= 3:
        rotorStartPos = startString
        return rotorStartPos

def ringSetting():
    rotor1 = str(clicked7.get())
    rotor2 = str(clicked8.get())
    rotor3 = str(clicked9.get())
    ringString = (rotor1+rotor2+rotor3)
    if len(ringString) >= 3:
        ringSetting = ringString
        return ringSetting


blackBackround = ImageTk.PhotoImage(Image.open("backround.jpg"))
woodBackround = ImageTk.PhotoImage(Image.open("woodBackround.jpg"))
paperBackround = ImageTk.PhotoImage(Image.open("paper.jfif"))

#FRAME CREATION
outterFrame = tk.Frame(root)
outterFrame.place(relx=0.025, rely=0.0, relwidth=0.45, relheight=1)
label = Label(outterFrame, image=woodBackround)
label.place(x=0, y=0, relwidth=1, relheight=1)

rotorFrame = tk.Frame(root, bg='gray')
rotorFrame.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.35)

label = Label(rotorFrame, image=blackBackround)
label.place(x=0, y=0, relwidth=1, relheight=1)

reflectorLabel = Label(rotorFrame, text="Reflector" ,bg="white")
reflectorLabel.place(relx=0.05, rely=0.1, relwidth=0.15, relheight=0.05)
rotor1Label = Label(rotorFrame, text="Rotor 1" ,bg="white")
rotor1Label.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.05)
rotor2Label = Label(rotorFrame, text="Rotor 2" ,bg="white")
rotor2Label.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.05)
rotor3Label = Label(rotorFrame, text="Rotor 3" ,bg="white")
rotor3Label.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.05)

rotor1LetterLabel = Label(rotorFrame, text="Start Letter" ,bg="white")
rotor1LetterLabel.place(relx=0.3, rely=0.4, relwidth=0.1, relheight=0.05)
rotor2LetterLabel = Label(rotorFrame, text="Start Letter" ,bg="white")
rotor2LetterLabel.place(relx=0.5, rely=0.4, relwidth=0.1, relheight=0.05)
rotor3LetterLabel = Label(rotorFrame, text="Start Letter" ,bg="white")
rotor3LetterLabel.place(relx=0.7, rely=0.4, relwidth=0.1, relheight=0.05)

rotor1RingSetting = Label(rotorFrame, text="Ring Setting" ,bg="white")
rotor1RingSetting.place(relx=0.3, rely=0.7, relwidth=0.1, relheight=0.05)
rotor2RingSetting = Label(rotorFrame, text="Ring Setting" ,bg="white")
rotor2RingSetting.place(relx=0.5, rely=0.7, relwidth=0.1, relheight=0.05)
rotor3RingSetting = Label(rotorFrame, text="Ring Setting" ,bg="white")
rotor3RingSetting.place(relx=0.7, rely=0.7, relwidth=0.1, relheight=0.05)

title = Label(outterFrame, text="ENIGMA M3", bg='gray', font=("Times", 40))
title.place(relx=0.25, rely=0.025, relwidth=0.45, relheight=0.05)
plain_text = Entry(root)
plain_text.pack(pady=20)

options = ["1", "2", "3", "4", "5"]
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clickedRef = StringVar()


#REFLECTOR DROPDOWN
rotorRef = OptionMenu(rotorFrame, clickedRef, "B", "C", command=rotorSelection)
rotorRef.place(relx=0.05, rely=0.16, relwidth=0.15, relheight=0.1)

#ROTOR DROPDOWNS
rotor1 = OptionMenu(rotorFrame, clicked1, *options, command=rotorSelection)
rotor1.place(relx=0.3, rely=0.16, relwidth=0.1, relheight=0.1)
rotor2 = OptionMenu(rotorFrame, clicked2, *options, command=rotorSelection)
rotor2.place(relx=0.5, rely=0.16, relwidth=0.1, relheight=0.1)
rotor3 = OptionMenu(rotorFrame, clicked3, *options, command=rotorSelection)
rotor3.place(relx=0.7, rely=0.16, relwidth=0.1, relheight=0.1)

clicked4 = StringVar()
clicked5 = StringVar()
clicked6 = StringVar()

rotor1Letter = OptionMenu(rotorFrame, clicked4, *alphabet, command=rotorSelection)
rotor1Letter.place(relx=0.3, rely=0.46, relwidth=0.1, relheight=0.1)
rotor2Letter = OptionMenu(rotorFrame, clicked5, *alphabet, command=rotorSelection)
rotor2Letter.place(relx=0.5, rely=0.46, relwidth=0.1, relheight=0.1)
rotor3Letter = OptionMenu(rotorFrame, clicked6, *alphabet, command=rotorSelection)
rotor3Letter.place(relx=0.7, rely=0.46, relwidth=0.1, relheight=0.1)

clicked7 = StringVar()
clicked8 = StringVar()
clicked9 = StringVar()

rotor1RingSetting = OptionMenu(rotorFrame, clicked7, *alphabet, command=rotorSelection)
rotor1RingSetting.place(relx=0.3, rely=0.76, relwidth=0.1, relheight=0.1)
rotor2RingSetting = OptionMenu(rotorFrame, clicked8, *alphabet, command=rotorSelection)
rotor2RingSetting.place(relx=0.5, rely=0.76, relwidth=0.1, relheight=0.1)
rotor3RingSetting = OptionMenu(rotorFrame, clicked9, *alphabet, command=rotorSelection)
rotor3RingSetting.place(relx=0.7, rely=0.76, relwidth=0.1, relheight=0.1)


inputTextLabel = Label(root, text="ENCRYPTED/DECRYPTED MESSAGE")
inputTextLabel.pack(pady=20)

submit_button = Button(root, text="Submit", command=encrypt)
submit_button.pack(pady=20)


def close(event):
    root.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing


root.bind('<Escape>', close)
root.mainloop()