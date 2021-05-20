import Enigma as eng
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
    if inputMessage.isalpha():
        inputMessage = inputMessage
    else:
        messagebox.showerror("INVALID INPUT!", "Letters only")

    var1 = rotorSelection(self=True)
    rotorString = var1[0]
    reflector = var1[1]
    rotorStartPos = startLetter()
    rotorRingSetting = ringSetting()
    plugboardSettings = x1
    encryptedMessage = eng.Enigma().encrypt(inputMessage, rotorString, rotorStartPos, plugboardSettings, reflector, rotorRingSetting)
    outputTextLabel.config(text=encryptedMessage)
    plugboardOutput.config(text=x1)
    return encryptedMessage

def rotorSelection(self):

    rotor1 = str(clicked1.get())
    rotor2 = str(clicked2.get())
    rotor3 = str(clicked3.get())
    rotorPos = (rotor1+rotor2+rotor3)
    reflector = str(clickedRef.get())
    if rotor1 == rotor2:
        messagebox.showerror("Input Error!", "Rotor " + rotor1 + " is already being used. Please select another rotor")
        clicked1.set("Rotor 1")
        clicked2.set("Rotor 2")
    elif rotor2 == rotor3:
        messagebox.showerror("Input Error!", "Rotor " + rotor2 + " is already being used. Please select another rotor")
        clicked2.set("Rotor 2")
        clicked3.set("Rotor 3")
    elif rotor1 == rotor3:
        messagebox.showerror("Input Error!", "Rotor " + rotor1 + " is already being used. Please select another rotor")
        clicked1.set("Rotor 1")
        clicked3.set("Rotor 3")
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
outterFrame.place(relx=0.275, rely=0.0, relwidth=0.45, relheight=1)
label = Label(outterFrame, image=paperBackround)
label.place(x=0, y=0, relwidth=1, relheight=1)
title = Label(outterFrame, text="ENIGMA M3", bg='black', fg='white', font=('Courier', 40))
title.pack(pady=40)

#ROTOR FRAME LABELS
rotorFrame = tk.Frame(root, bg='gray')
rotorFrame.place(relx=0.295, rely=0.11, relwidth=0.41, relheight=0.3)
label = Label(rotorFrame, image=blackBackround)
label.place(x=0, y=0, relwidth=1, relheight=1)
rotorSettingsLabel = Label(rotorFrame, text="ROTOR SETTINGS", bg='SteelBlue1', font=('Courier', 20))
rotorSettingsLabel.pack(pady=20)


#PLUGBOARD FRAME LABELS
plugboardFrame = tk.Frame(root, bg='gray')
plugboardFrame.place(relx=0.295, rely=0.42, relwidth=0.41, relheight=0.3)
plugboardLabel = Label(plugboardFrame, image=blackBackround)
plugboardLabel.place(x=0, y=0, relwidth=1, relheight=1)
plugboardTitle = Label(plugboardFrame, text="PLUGBOARD SETTINGS", bg='SteelBlue1', font=('Courier', 20))
plugboardTitle.pack(pady=15)
plugboardOutput = Label(plugboardFrame)
plugboardOutput.place(relx=0.325, rely=0.7, relwidth=0.35, relheight=0.1)

#OUTPUT FRAME LABELS
finalFrame = Frame(outterFrame)
finalFrame.place(relx=0.045, rely=0.73, relwidth=0.91, relheight=0.25)
label = Label(finalFrame, image=blackBackround)
label.place(x=0, y=0, relwidth=1, relheight=1)
inputTextLabel = Label(finalFrame, text="Input message:", bg='gray', font=20)
inputTextLabel.place(relx=0.05, rely=0.15, relwidth=0.3, relheight=0.2)
plain_text = Entry(finalFrame, justify='center', font=20)
plain_text.place(relx=0.05, rely=0.4, relwidth=0.3, relheight=0.2)
inputTextLabel = Label(finalFrame, text="Output message:", bg='gray', font=20)
inputTextLabel.place(relx=0.65, rely=0.15, relwidth=0.3, relheight=0.2)
outputTextLabel = Label(finalFrame, font=18)
outputTextLabel.place(relx=0.65, rely=0.4, relwidth=0.3, relheight=0.2)

submit_button = Button(finalFrame, text="Encrypt / Decrypt", font=20, command=encrypt)
submit_button.pack(pady=100)


reflectorLabel = Label(rotorFrame, text="Reflector" ,bg="white")
reflectorLabel.place(relx=0.05, rely=0.26, relwidth=0.15, relheight=0.05)
rotor1Label = Label(rotorFrame, text="Rotor 1" ,bg="white")
rotor1Label.place(relx=0.3, rely=0.26, relwidth=0.1, relheight=0.05)
rotor2Label = Label(rotorFrame, text="Rotor 2" ,bg="white")
rotor2Label.place(relx=0.5, rely=0.26, relwidth=0.1, relheight=0.05)
rotor3Label = Label(rotorFrame, text="Rotor 3" ,bg="white")
rotor3Label.place(relx=0.7, rely=0.26, relwidth=0.1, relheight=0.05)

rotor1LetterLabel = Label(rotorFrame, text="Start Letter" ,bg="white")
rotor1LetterLabel.place(relx=0.3, rely=0.5, relwidth=0.1, relheight=0.05)
rotor2LetterLabel = Label(rotorFrame, text="Start Letter" ,bg="white")
rotor2LetterLabel.place(relx=0.5, rely=0.5, relwidth=0.1, relheight=0.05)
rotor3LetterLabel = Label(rotorFrame, text="Start Letter" ,bg="white")
rotor3LetterLabel.place(relx=0.7, rely=0.5, relwidth=0.1, relheight=0.05)

rotor1RingSetting = Label(rotorFrame, text="Ring Setting" ,bg="white")
rotor1RingSetting.place(relx=0.3, rely=0.74, relwidth=0.1, relheight=0.05)
rotor2RingSetting = Label(rotorFrame, text="Ring Setting" ,bg="white")
rotor2RingSetting.place(relx=0.5, rely=0.74, relwidth=0.1, relheight=0.05)
rotor3RingSetting = Label(rotorFrame, text="Ring Setting" ,bg="white")
rotor3RingSetting.place(relx=0.7, rely=0.74, relwidth=0.1, relheight=0.05)

options = ["1", "2", "3", "4", "5"]
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

clicked1 = StringVar()
clicked1.set("Rotor 1")
clicked2 = StringVar()
clicked2.set("Rotor 2")
clicked3 = StringVar()
clicked3.set("Rotor 3")
clickedRef = StringVar()


#REFLECTOR DROPDOWN
rotorRef = OptionMenu(rotorFrame, clickedRef, "B", "C", command=rotorSelection)
rotorRef.place(relx=0.05, rely=0.32, relwidth=0.15, relheight=0.1)

#ROTOR DROPDOWNS
rotor1 = OptionMenu(rotorFrame, clicked1, "Rotor 1", *options, command=rotorSelection)
rotor1.place(relx=0.3, rely=0.32, relwidth=0.1, relheight=0.1)

rotor2 = OptionMenu(rotorFrame, clicked2, *options, command=rotorSelection)
rotor2.place(relx=0.5, rely=0.32, relwidth=0.1, relheight=0.1)
rotor3 = OptionMenu(rotorFrame, clicked3, *options, command=rotorSelection)
rotor3.place(relx=0.7, rely=0.32, relwidth=0.1, relheight=0.1)

clicked4 = StringVar()
clicked5 = StringVar()
clicked6 = StringVar()

rotor1Letter = OptionMenu(rotorFrame, clicked4, *alphabet, command=rotorSelection)
rotor1Letter.place(relx=0.3, rely=0.56, relwidth=0.1, relheight=0.1)
rotor2Letter = OptionMenu(rotorFrame, clicked5, *alphabet, command=rotorSelection)
rotor2Letter.place(relx=0.5, rely=0.56, relwidth=0.1, relheight=0.1)
rotor3Letter = OptionMenu(rotorFrame, clicked6, *alphabet, command=rotorSelection)
rotor3Letter.place(relx=0.7, rely=0.56, relwidth=0.1, relheight=0.1)

clicked7 = StringVar()
clicked8 = StringVar()
clicked9 = StringVar()

rotor1RingSetting = OptionMenu(rotorFrame, clicked7, *alphabet, command=rotorSelection)
rotor1RingSetting.place(relx=0.3, rely=0.8, relwidth=0.1, relheight=0.1)
rotor2RingSetting = OptionMenu(rotorFrame, clicked8, *alphabet, command=rotorSelection)
rotor2RingSetting.place(relx=0.5, rely=0.8, relwidth=0.1, relheight=0.1)
rotor3RingSetting = OptionMenu(rotorFrame, clicked9, *alphabet, command=rotorSelection)
rotor3RingSetting.place(relx=0.7, rely=0.8, relwidth=0.1, relheight=0.1)

answer_list = []
x1 = ""
oddList = []
evenList = []

def button_click(b, letter):
    global answer_list, oddList, evenList, x1

    if letter not in answer_list:
        answer_list.append(letter)
        b.configure(state=tk.DISABLED)
    else:
        messagebox.showerror("Error!", letter + " has already been selected!")
        errorLetter = answer_list[-1]
        if errorLetter != letter:
            del answer_list[-1]

    if (len(answer_list) % 2) == 1:
        num = answer_list[-1:]
        num = (", ".join(num))
        oddList.append(num)

    else:
        num2 = answer_list[-1:]
        num2 = (", ".join(num2))
        evenList.append(num2)

    x1 = [''.join(i) for i in zip(answer_list[::2], answer_list[1::2])]


    if len(answer_list) <= 2:
        b.configure(bg='green')
    elif len(answer_list) > 2 and len(answer_list) <= 4:
        b.configure(bg='yellow')
    elif len(answer_list) > 4 and len(answer_list) <= 6:
        b.configure(bg='red')
    elif len(answer_list) > 6 and len(answer_list) <= 8:
        b.configure(bg='blue')
    elif len(answer_list) > 8 and len(answer_list) <= 10:
        b.configure(bg='brown')
    elif len(answer_list) > 10 and len(answer_list) <= 12:
        b.configure(bg='pink')
    elif len(answer_list) > 12 and len(answer_list) <= 14:
        b.configure(bg='light cyan')
    elif len(answer_list) > 14 and len(answer_list) <= 16:
        b.configure(bg='pale green')
    elif len(answer_list) > 16 and len(answer_list) <= 18:
        b.configure(bg='DarkOliveGreen2')
    elif len(answer_list) > 18 and len(answer_list) <= 20:
        b.configure(bg='black')
    elif len(answer_list) > 20:
        b.configure(state=tk.NORMAL, bg='white')

    if len(x1) > 10 and len(answer_list) > 20:
        messagebox.showerror("Input Error!", "Max plugboard pairs = 10." )
        del answer_list[-2:]
        del x1[-1:]

    plugboardOutput.config(text=x1)


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
buttonQ.place(relx=0.05, rely=0.2, relwidth=0.07, relheight=0.1)
buttonW.place(relx=0.14, rely=0.2, relwidth=0.07, relheight=0.1)
buttonE.place(relx=0.23, rely=0.2, relwidth=0.07, relheight=0.1)
buttonR.place(relx=0.32, rely=0.2, relwidth=0.07, relheight=0.1)
buttonT.place(relx=0.41, rely=0.2, relwidth=0.07, relheight=0.1)
buttonY.place(relx=0.50, rely=0.2, relwidth=0.07, relheight=0.1)
buttonU.place(relx=0.59, rely=0.2, relwidth=0.07, relheight=0.1)
buttonI.place(relx=0.68, rely=0.2, relwidth=0.07, relheight=0.1)
buttonO.place(relx=0.77, rely=0.2, relwidth=0.07, relheight=0.1)
buttonP.place(relx=0.86, rely=0.2, relwidth=0.07, relheight=0.1)


#MIDDLE PLUGBOARD ROW
buttonA.place(relx=0.09, rely=0.35, relwidth=0.07, relheight=0.1)
buttonS.place(relx=0.18, rely=0.35, relwidth=0.07, relheight=0.1)
buttonD.place(relx=0.27, rely=0.35, relwidth=0.07, relheight=0.1)
buttonF.place(relx=0.36, rely=0.35, relwidth=0.07, relheight=0.1)
buttonG.place(relx=0.45, rely=0.35, relwidth=0.07, relheight=0.1)
buttonH.place(relx=0.54, rely=0.35, relwidth=0.07, relheight=0.1)
buttonJ.place(relx=0.63, rely=0.35, relwidth=0.07, relheight=0.1)
buttonK.place(relx=0.72, rely=0.35, relwidth=0.07, relheight=0.1)
buttonL.place(relx=0.81, rely=0.35, relwidth=0.07, relheight=0.1)


#BOTTOM PLUGBOARD ROW
buttonZ.place(relx=0.14, rely=0.5, relwidth=0.07, relheight=0.1)
buttonX.place(relx=0.23, rely=0.5, relwidth=0.07, relheight=0.1)
buttonC.place(relx=0.32, rely=0.5, relwidth=0.07, relheight=0.1)
buttonV.place(relx=0.41, rely=0.5, relwidth=0.07, relheight=0.1)
buttonB.place(relx=0.50, rely=0.5, relwidth=0.07, relheight=0.1)
buttonN.place(relx=0.59, rely=0.5, relwidth=0.07, relheight=0.1)
buttonM.place(relx=0.68, rely=0.5, relwidth=0.07, relheight=0.1)

def clearPlugboard():
    buttonA.configure(state=tk.NORMAL, bg='white')
    buttonB.configure(state=tk.NORMAL, bg='white')
    buttonC.configure(state=tk.NORMAL, bg='white')
    buttonD.configure(state=tk.NORMAL, bg='white')
    buttonE.configure(state=tk.NORMAL, bg='white')
    buttonF.configure(state=tk.NORMAL, bg='white')
    buttonG.configure(state=tk.NORMAL, bg='white')
    buttonH.configure(state=tk.NORMAL, bg='white')
    buttonI.configure(state=tk.NORMAL, bg='white')
    buttonJ.configure(state=tk.NORMAL, bg='white')
    buttonK.configure(state=tk.NORMAL, bg='white')
    buttonL.configure(state=tk.NORMAL, bg='white')
    buttonM.configure(state=tk.NORMAL, bg='white')
    buttonN.configure(state=tk.NORMAL, bg='white')
    buttonO.configure(state=tk.NORMAL, bg='white')
    buttonP.configure(state=tk.NORMAL, bg='white')
    buttonQ.configure(state=tk.NORMAL, bg='white')
    buttonR.configure(state=tk.NORMAL, bg='white')
    buttonS.configure(state=tk.NORMAL, bg='white')
    buttonT.configure(state=tk.NORMAL, bg='white')
    buttonU.configure(state=tk.NORMAL, bg='white')
    buttonV.configure(state=tk.NORMAL, bg='white')
    buttonW.configure(state=tk.NORMAL, bg='white')
    buttonX.configure(state=tk.NORMAL, bg='white')
    buttonY.configure(state=tk.NORMAL, bg='white')
    buttonZ.configure(state=tk.NORMAL, bg='white')
    answer_list.clear()
    x1.clear()
    plugboardOutput.config(text="")

def close(event):
    root.withdraw()
    sys.exit()

clearButton = Button(plugboardFrame, text="Clear selections", font=20, command=clearPlugboard)
clearButton.place(relx=0.325, rely=0.85, relwidth=0.35, relheight=0.1)

root.bind('<Escape>', close)
root.mainloop()