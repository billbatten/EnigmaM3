# from tkinter import messagebox
#
# import Enigma
# import tkinter as tk
# from tkinter import *
# import sys
# from PIL import ImageTk, Image
#
# root = tk.Tk()
# root.attributes('-fullscreen', True)
# root.configure(bg='#404040')
#
#
# def encrypt():
#     inputMessage = plain_text.get()
#     var1 = rotorSelection(self=True)
#     rotorString = var1[0]
#     reflector = var1[1]
#     rotorStartPos = startLetter()
#     rotorRingSetting = ringSetting()
#     plugboardSettings = x1
#     encryptedMessage = Enigma.encrypt(inputMessage, rotorString, rotorStartPos, plugboardSettings, reflector, rotorRingSetting)
#     inputTextLabel.config(text=encryptedMessage)
#     return encryptedMessage
#
# def rotorSelection(self):
#
#     rotor1 = str(clicked1.get())
#     rotor2 = str(clicked2.get())
#     rotor3 = str(clicked3.get())
#     rotorPos = (rotor1+rotor2+rotor3)
#     reflector = str(clickedRef.get())
#     if len(rotorPos) >= 3:
#         finalRotorPosition = rotorPos
#         return finalRotorPosition, reflector
#
# def startLetter():
#     rotor1 = str(clicked4.get())
#     rotor2 = str(clicked5.get())
#     rotor3 = str(clicked6.get())
#     startString = (rotor1+rotor2+rotor3)
#     if len(startString) >= 3:
#         rotorStartPos = startString
#         return rotorStartPos
#
# def ringSetting():
#     rotor1 = str(clicked7.get())
#     rotor2 = str(clicked8.get())
#     rotor3 = str(clicked9.get())
#     ringString = (rotor1+rotor2+rotor3)
#     if len(ringString) >= 3:
#         ringSetting = ringString
#         return ringSetting
#
# answer_list = []
# oddList = []
# evenList = []
# x1 = ""
#
# def button_click(b, letter):
#     global answer_list, oddList, evenList, x1
#     if letter not in answer_list:
#         answer_list.append(letter)
#         b.configure(bg='red')
#     else:
#         messagebox.showerror("Error!", letter + " has already been selected!")
#
#     if (len(answer_list) % 2) == 1:
#         num = answer_list[-1:]
#         num = (", ".join(num))
#         oddList.append(num)
#
#     else:
#         num2 = answer_list[-1:]
#         num2 = (", ".join(num2))
#         evenList.append(num2)
#
#     x1 = [''.join(i) for i in zip(answer_list[::2], answer_list[1::2])]
#
#     return x1
#
#
# blackBackround = ImageTk.PhotoImage(Image.open("backround.jpg"))
# woodBackround = ImageTk.PhotoImage(Image.open("woodBackround.jpg"))
# paperBackround = ImageTk.PhotoImage(Image.open("paper.jfif"))
#
# #FRAME CREATION
# outterFrame = tk.Frame(root)
# outterFrame.place(relx=0.025, rely=0.0, relwidth=0.45, relheight=1)
# label = Label(outterFrame, image=woodBackround)
# label.place(x=0, y=0, relwidth=1, relheight=1)
#
# #ROTOR FRAME SECTION
# #Any widgets linked to the rotors are placed in this section
# rotorFrame = tk.Frame(root, bg='gray')
# rotorFrame.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.35)
# label = Label(rotorFrame, image=blackBackround)
# label.place(x=0, y=0, relwidth=1, relheight=1)
#
# reflectorLabel = Label(rotorFrame, text="Reflector" ,bg="white")
# reflectorLabel.place(relx=0.05, rely=0.1, relwidth=0.15, relheight=0.05)
# rotor1Label = Label(rotorFrame, text="Rotor 1" ,bg="white")
# rotor1Label.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.05)
# rotor2Label = Label(rotorFrame, text="Rotor 2" ,bg="white")
# rotor2Label.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.05)
# rotor3Label = Label(rotorFrame, text="Rotor 3" ,bg="white")
# rotor3Label.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.05)
#
# rotor1LetterLabel = Label(rotorFrame, text="Start Letter" ,bg="white")
# rotor1LetterLabel.place(relx=0.3, rely=0.4, relwidth=0.1, relheight=0.05)
# rotor2LetterLabel = Label(rotorFrame, text="Start Letter" ,bg="white")
# rotor2LetterLabel.place(relx=0.5, rely=0.4, relwidth=0.1, relheight=0.05)
# rotor3LetterLabel = Label(rotorFrame, text="Start Letter" ,bg="white")
# rotor3LetterLabel.place(relx=0.7, rely=0.4, relwidth=0.1, relheight=0.05)
#
# rotor1RingSetting = Label(rotorFrame, text="Ring Setting" ,bg="white")
# rotor1RingSetting.place(relx=0.3, rely=0.7, relwidth=0.1, relheight=0.05)
# rotor2RingSetting = Label(rotorFrame, text="Ring Setting" ,bg="white")
# rotor2RingSetting.place(relx=0.5, rely=0.7, relwidth=0.1, relheight=0.05)
# rotor3RingSetting = Label(rotorFrame, text="Ring Setting" ,bg="white")
# rotor3RingSetting.place(relx=0.7, rely=0.7, relwidth=0.1, relheight=0.05)
#
# title = Label(outterFrame, text="ENIGMA M3", bg='gray', font=("Times", 40))
# title.place(relx=0.25, rely=0.025, relwidth=0.45, relheight=0.05)
#
# paperFrame = tk.Frame(root)
# paperFrame.place(relx=0.525, rely=0.0, relwidth=0.45, relheight=1)
#
# label = Label(paperFrame, image=paperBackround)
# label.place(x=0, y=0, relwidth=1, relheight=1)
#
#
#
# label = Label(paperFrame, text="Enter Message to Encrypt/Decrypt: ")
# label.pack(pady=10)
# plain_text = Entry(paperFrame)
# plain_text.pack(pady=0)
#
# label = Label(paperFrame, text="Encrypted/Decrypted Message: ")
# label.pack(pady=10)
# inputTextLabel = Label(paperFrame)
# inputTextLabel.pack(pady=20)
#
# submit_button = Button(paperFrame, text="Submit", command=encrypt)
# submit_button.pack(pady=20)
#
# options = ["1", "2", "3", "4", "5"]
#
# alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#
# clicked1 = StringVar()
# clicked2 = StringVar()
# clicked3 = StringVar()
# clickedRef = StringVar()
#
# #REFLECTOR DROPDOWN
# rotorRef = OptionMenu(rotorFrame, clickedRef, "B", "C", command=lambda : rotorSelection())
# rotorRef.place(relx=0.05, rely=0.16, relwidth=0.15, relheight=0.1)
#
# #ROTOR DROPDOWNS
# rotor1Options = OptionMenu(rotorFrame, clicked1, *options, command=rotorSelection)
# rotor1Options.place(relx=0.3, rely=0.16, relwidth=0.1, relheight=0.1)
# rotor2Options = OptionMenu(rotorFrame, clicked2, *options, command=rotorSelection)
# rotor2Options.place(relx=0.5, rely=0.16, relwidth=0.1, relheight=0.1)
# rotor3Options = OptionMenu(rotorFrame, clicked3, *options, command=rotorSelection)
# rotor3Options.place(relx=0.7, rely=0.16, relwidth=0.1, relheight=0.1)
#
# clicked4 = StringVar()
# clicked5 = StringVar()
# clicked6 = StringVar()
#
# rotor1Letter = OptionMenu(rotorFrame, clicked4, *alphabet, command=rotorSelection)
# rotor1Letter.place(relx=0.3, rely=0.46, relwidth=0.1, relheight=0.1)
# rotor2Letter = OptionMenu(rotorFrame, clicked5, *alphabet, command=rotorSelection)
# rotor2Letter.place(relx=0.5, rely=0.46, relwidth=0.1, relheight=0.1)
# rotor3Letter = OptionMenu(rotorFrame, clicked6, *alphabet, command=rotorSelection)
# rotor3Letter.place(relx=0.7, rely=0.46, relwidth=0.1, relheight=0.1)
#
# clicked7 = StringVar()
# clicked8 = StringVar()
# clicked9 = StringVar()
#
# rotor1RingSetting = OptionMenu(rotorFrame, clicked7, *alphabet, command=rotorSelection)
# rotor1RingSetting.place(relx=0.3, rely=0.76, relwidth=0.1, relheight=0.1)
# rotor2RingSetting = OptionMenu(rotorFrame, clicked8, *alphabet, command=rotorSelection)
# rotor2RingSetting.place(relx=0.5, rely=0.76, relwidth=0.1, relheight=0.1)
# rotor3RingSetting = OptionMenu(rotorFrame, clicked9, *alphabet, command=rotorSelection)
# rotor3RingSetting.place(relx=0.7, rely=0.76, relwidth=0.1, relheight=0.1)
#
#
# plugboardFrame = tk.Frame(root, bg='gray')
# plugboardFrame.place(relx=0.05, rely=0.6, relwidth=0.4, relheight=0.35)
# label = Label(plugboardFrame, image=blackBackround)
# label.place(x=0, y=0, relwidth=1, relheight=1)
# label2 = Label(plugboardFrame)
# label2.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.15)
#
#
#
# buttonA = Button(plugboardFrame, text='A', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(buttonA, "A"))
# buttonB = Button(plugboardFrame, text='B', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(buttonB, "B"))
# buttonC = Button(plugboardFrame, text='C', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(buttonC, "C"))
# buttonD = Button(plugboardFrame, text='D', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(buttonD, "D"))
# buttonE = Button(plugboardFrame, text='E', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(buttonE, "E"))
# buttonF = Button(plugboardFrame, text='F', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(buttonF, "F"))
# buttonG = Button(plugboardFrame, text='G', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(buttonG, "G"))
# buttonH = Button(plugboardFrame, text='H', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(buttonH, "H"))
# buttonI = Button(plugboardFrame, text='I', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(buttonI, "I"))
# buttonJ = Button(plugboardFrame, text='J', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(buttonJ, "J"))
# buttonK = Button(plugboardFrame, text='K', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(buttonK, "K"))
# buttonL = Button(plugboardFrame, text='L', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(buttonL, "L"))
#
# buttonA.grid(row=0, column=0)
# buttonB.grid(row=0, column=1)
# buttonC.grid(row=0, column=2)
# buttonD.grid(row=0, column=3)
#
# buttonE.grid(row=1, column=0)
# buttonF.grid(row=1, column=1)
# buttonG.grid(row=1, column=2)
# buttonH.grid(row=1, column=3)
#
# buttonI.grid(row=2, column=0)
# buttonJ.grid(row=2, column=1)
# buttonK.grid(row=2, column=2)
# buttonL.grid(row=2, column=3)
#
#
# def close(event):
#     root.withdraw() # if you want to bring it back
#     sys.exit() # if you want to exit the entire thing
#
#
# root.bind('<Escape>', close)
# root.mainloop()

import Enigma
import tkinter as tk
from tkinter import *
import sys
from PIL import ImageTk, Image
from tkinter import messagebox

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='black')


def encrypt():
    inputMessage = plain_text.get()
    var1 = rotorSelection(self=True)
    rotorString = var1[0]
    reflector = var1[1]
    rotorStartPos = startLetter()
    rotorRingSetting = ringSetting()
    plugboardSettings = x1
    print()
    encryptedMessage = Enigma.encrypt(inputMessage, rotorString, rotorStartPos, plugboardSettings, reflector, rotorRingSetting)
    inputTextLabel.config(text=encryptedMessage)
    plugboardOutput.config(text=x1)
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
title = Label(outterFrame, text="ENIGMA M3", bg='black', fg='white', font=("Times", 35))
title.place(relx=0.25, rely=0.015, relwidth=0.45, relheight=0.05)

rotorFrame = tk.Frame(root, bg='gray')
rotorFrame.place(relx=0.045, rely=0.07, relwidth=0.41, relheight=0.3)
label = Label(rotorFrame, image=blackBackround)
label.place(x=0, y=0, relwidth=1, relheight=1)

plugboardFrame = tk.Frame(root, bg='gray')
plugboardFrame.place(relx=0.045, rely=0.38, relwidth=0.41, relheight=0.25)
plugboardLabel = Label(plugboardFrame, image=blackBackround)
plugboardLabel.place(x=0, y=0, relwidth=1, relheight=1)
plugboardOutput = Label(plugboardFrame)
#plugboardOutput.place(relx=0.3, rely=0.6, relwidth=0.35, relheight=0.15)

outputFrame = tk.Frame(root, bg='gray')
outputFrame.place(relx=0.5, rely=0.0, relwidth=0.45, relheight=1)
outputFrameImage = Label(outputFrame, image=paperBackround)
outputFrameImage.place(x=0, y=0, relwidth=1, relheight=1)
inputTextLabel = Label(outputFrame, text="ENCRYPTED/DECRYPTED MESSAGE")
inputTextLabel.pack(pady=20)
plain_text = Entry(outputFrame)
plain_text.pack(pady=20)
submit_button = Button(outputFrame, text="Submit", command=encrypt)
submit_button.pack(pady=20)


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

answer_list = []
oddList = []
evenList = []
x1 = ""
button_ids = []

def button_click(b, letter):
    global answer_list, oddList, evenList, x1

    if letter not in answer_list:
        answer_list.append(letter)
        print(answer_list)
    else:
        messagebox.showerror("Error!", letter + " has already been selected!")
        b.configure(bg='white')
        #print(answer_list)
        errorLetter = answer_list[-1]
        print(errorLetter)
        if errorLetter != letter:
            del answer_list[-1]
        print(letter)
        print(answer_list)
        #print(answer_list)

    if (len(answer_list) % 2) == 1:
        num = answer_list[-1:]
        num = (", ".join(num))
        oddList.append(num)

    else:
        num2 = answer_list[-1:]
        num2 = (", ".join(num2))
        evenList.append(num2)

        x1 = [''.join(i) for i in zip(answer_list[::2], answer_list[1::2])]
    #print("x1 = ", x1)

    if len(x1) > 10:
        messagebox.showerror("Input Error!", "Max plugboard pairs = 10." )
    plugboardOutput.config(text=x1)
    b.configure(bg='yellow')
    print(x1)
    return x1

buttonA = Button(plugboardFrame, text='A', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonA, "A"))
buttonB = Button(plugboardFrame, text='B', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonB, "B"))
buttonC = Button(plugboardFrame, text='C', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonC, "C"))
buttonD = Button(plugboardFrame, text='D', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonD, "D"))
buttonE = Button(plugboardFrame, text='E', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonE, "E"))
buttonF = Button(plugboardFrame, text='F', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonF, "F"))
buttonG = Button(plugboardFrame, text='G', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonG, "G"))
buttonH = Button(plugboardFrame, text='H', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonH, "H"))
buttonI = Button(plugboardFrame, text='I', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonI, "I"))
buttonJ = Button(plugboardFrame, text='J', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonJ, "J"))
buttonK = Button(plugboardFrame, text='K', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonK, "K"))
buttonL = Button(plugboardFrame, text='L', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonL, "L"))
buttonM = Button(plugboardFrame, text='M', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonM, "M"))
buttonN = Button(plugboardFrame, text='N', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonN, "N"))
buttonO = Button(plugboardFrame, text='O', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonO, "O"))
buttonP = Button(plugboardFrame, text='P', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonP, "P"))
buttonQ = Button(plugboardFrame, text='Q', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonQ, "Q"))
buttonR = Button(plugboardFrame, text='R', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonR, "R"))
buttonS = Button(plugboardFrame, text='S', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonS, "S"))
buttonT = Button(plugboardFrame, text='T', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonT, "T"))
buttonU = Button(plugboardFrame, text='U', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonU, "U"))
buttonV = Button(plugboardFrame, text='V', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonV, "V"))
buttonW = Button(plugboardFrame, text='W', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonW, "W"))
buttonX = Button(plugboardFrame, text='X', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonX, "X"))
buttonY = Button(plugboardFrame, text='Y', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonY, "Y"))
buttonZ = Button(plugboardFrame, text='Z', font=("Helvetica", 15), height=1, width=3, command=lambda: button_click(buttonZ, "Z"))

#TOP PLUGBOARD ROW
buttonQ.place(relx=0.05, rely=0.05, relwidth=0.07, relheight=0.1)
buttonW.place(relx=0.14, rely=0.05, relwidth=0.07, relheight=0.1)
buttonE.place(relx=0.23, rely=0.05, relwidth=0.07, relheight=0.1)
buttonR.place(relx=0.32, rely=0.05, relwidth=0.07, relheight=0.1)
buttonT.place(relx=0.41, rely=0.05, relwidth=0.07, relheight=0.1)
buttonY.place(relx=0.50, rely=0.05, relwidth=0.07, relheight=0.1)
buttonU.place(relx=0.59, rely=0.05, relwidth=0.07, relheight=0.1)
buttonI.place(relx=0.68, rely=0.05, relwidth=0.07, relheight=0.1)
buttonO.place(relx=0.77, rely=0.05, relwidth=0.07, relheight=0.1)
buttonP.place(relx=0.86, rely=0.05, relwidth=0.07, relheight=0.1)


#MIDDLE PLUGBOARD ROW
buttonA.place(relx=0.09, rely=0.2, relwidth=0.07, relheight=0.1)
buttonS.place(relx=0.18, rely=0.2, relwidth=0.07, relheight=0.1)
buttonD.place(relx=0.27, rely=0.2, relwidth=0.07, relheight=0.1)
buttonF.place(relx=0.36, rely=0.2, relwidth=0.07, relheight=0.1)
buttonG.place(relx=0.45, rely=0.2, relwidth=0.07, relheight=0.1)
buttonH.place(relx=0.54, rely=0.2, relwidth=0.07, relheight=0.1)
buttonJ.place(relx=0.63, rely=0.2, relwidth=0.07, relheight=0.1)
buttonK.place(relx=0.72, rely=0.2, relwidth=0.07, relheight=0.1)
buttonL.place(relx=0.81, rely=0.2, relwidth=0.07, relheight=0.1)


#BOTTOM PLUGBOARD ROW
buttonZ.place(relx=0.14, rely=0.35, relwidth=0.07, relheight=0.1)
buttonX.place(relx=0.23, rely=0.35, relwidth=0.07, relheight=0.1)
buttonC.place(relx=0.32, rely=0.35, relwidth=0.07, relheight=0.1)
buttonV.place(relx=0.41, rely=0.35, relwidth=0.07, relheight=0.1)
buttonB.place(relx=0.50, rely=0.35, relwidth=0.07, relheight=0.1)
buttonN.place(relx=0.59, rely=0.35, relwidth=0.07, relheight=0.1)
buttonM.place(relx=0.68, rely=0.35, relwidth=0.07, relheight=0.1)


def close(event):
    root.withdraw()
    sys.exit()

root.bind('<Escape>', close)
root.mainloop()
