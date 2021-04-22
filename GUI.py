#.pack()
from Enigma import *
import tkinter as tk
from tkinter import *



HEIGHT = 950
WIDTH = 1800

root = tk.Tk() #Fits all the GUI in
root.attributes('-fullscreen', True)

canvas = tk.Canvas(root, bg='#333333', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)


#FRAME CREATION
rotorFrame = tk.Frame(root, bg='gray')
rotorFrame.place(relx=0.3, rely=0.05, relwidth=0.4, relheight=0.3)

keyboardFrame = tk.Frame(root, bg='white')
keyboardFrame.place(relx=0.3, rely=0.36, relwidth=0.4, relheight=0.3)

plugboardFrame = tk.Frame(root, bg='gray')
plugboardFrame.place(relx=0.3, rely=0.67, relwidth=0.4, relheight=0.3)


#ROTOR FRAME




#TOP KEYBOARD ROW

letterQ = tk.Button(keyboardFrame,text='Q', borderwidth=2, bg='#808080')
letterQ.place(relx=0.07, rely=0.12, relwidth=0.07, relheight=0.17)

letterW = tk.Button(keyboardFrame, text='W', borderwidth=2, bg='#808080')
letterW.place(relx=0.15, rely=0.12, relwidth=0.07, relheight=0.17)

letterE = tk.Button(keyboardFrame, text='E', borderwidth=2, bg='#808080')
letterE.place(relx=0.23, rely=0.12, relwidth=0.07, relheight=0.17)

letterR = tk.Button(keyboardFrame, text='R', borderwidth=2, bg='#808080')
letterR.place(relx=0.31, rely=0.12, relwidth=0.07, relheight=0.17)

letterT = tk.Button(keyboardFrame, text='T', borderwidth=2, bg='#808080')
letterT.place(relx=0.39, rely=0.12, relwidth=0.07, relheight=0.17)

letterY = tk.Button(keyboardFrame, text='Y', borderwidth=2, bg='#808080')
letterY.place(relx=0.47, rely=0.12, relwidth=0.07, relheight=0.17)

letterU = tk.Button(keyboardFrame, text='U', borderwidth=2, bg='#808080')
letterU.place(relx=0.55, rely=0.12, relwidth=0.07, relheight=0.17)

letterI = tk.Button(keyboardFrame, text='I', borderwidth=2, bg='#808080')
letterI.place(relx=0.63, rely=0.12, relwidth=0.07, relheight=0.17)

letterO = tk.Button(keyboardFrame, text='O', borderwidth=2, bg='#808080')
letterO.place(relx=0.71, rely=0.12, relwidth=0.07, relheight=0.17)

letterP = tk.Button(keyboardFrame, text='P', borderwidth=2, bg='#808080')
letterP.place(relx=0.79, rely=0.12, relwidth=0.07, relheight=0.17)

#MIDDLE KEYBOARD ROW

letterA = tk.Button(keyboardFrame, text='A', borderwidth=2, bg='#808080')
letterA.place(relx=0.13, rely=0.37, relwidth=0.07, relheight=0.17)

letterS = tk.Button(keyboardFrame, text='S', borderwidth=2, bg='#808080')
letterS.place(relx=0.21, rely=0.37, relwidth=0.07, relheight=0.17)

letterD = tk.Button(keyboardFrame, text='D', borderwidth=2, bg='#808080')
letterD.place(relx=0.29, rely=0.37, relwidth=0.07, relheight=0.17)

letterF = tk.Button(keyboardFrame, text='F', borderwidth=2, bg='#808080')
letterF.place(relx=0.37, rely=0.37, relwidth=0.07, relheight=0.17)

letterG = tk.Button(keyboardFrame, text='G', borderwidth=2, bg='#808080')
letterG.place(relx=0.45, rely=0.37, relwidth=0.07, relheight=0.17)

letterH = tk.Button(keyboardFrame, text='H', borderwidth=2, bg='#808080')
letterH.place(relx=0.53, rely=0.37, relwidth=0.07, relheight=0.17)

letterJ = tk.Button(keyboardFrame, text='J', borderwidth=2, bg='#808080')
letterJ.place(relx=0.61, rely=0.37, relwidth=0.07, relheight=0.17)

letterK = tk.Button(keyboardFrame, text='K', borderwidth=2, bg='#808080')
letterK.place(relx=0.69, rely=0.37, relwidth=0.07, relheight=0.17)

letterL = tk.Button(keyboardFrame, text='L', borderwidth=2, bg='#808080')
letterL.place(relx=0.77, rely=0.37, relwidth=0.07, relheight=0.17)


#BOTTOM KEYBOARD ROW

letterZ = tk.Button(keyboardFrame, text='Z', borderwidth=2, bg='#808080')
letterZ.place(relx=0.20, rely=0.62, relwidth=0.07, relheight=0.17)

letterX = tk.Button(keyboardFrame, text='X', borderwidth=2, bg='#808080')
letterX.place(relx=0.28, rely=0.62, relwidth=0.07, relheight=0.17)

letterC = tk.Button(keyboardFrame, text='C', borderwidth=2, bg='#808080')
letterC.place(relx=0.36, rely=0.62, relwidth=0.07, relheight=0.17)

letterV = tk.Button(keyboardFrame, text='V', borderwidth=2, bg='#808080')
letterV.place(relx=0.44, rely=0.62, relwidth=0.07, relheight=0.17)

letterB = tk.Button(keyboardFrame, text='B', borderwidth=2, bg='#808080')
letterB.place(relx=0.52, rely=0.62, relwidth=0.07, relheight=0.17)

letterN = tk.Button(keyboardFrame, text='N', borderwidth=2, bg='#808080')
letterN.place(relx=0.60, rely=0.62, relwidth=0.07, relheight=0.17)

letterM = tk.Button(keyboardFrame, text='M', borderwidth=2, bg='#808080')
letterM.place(relx=0.68, rely=0.62, relwidth=0.07, relheight=0.17)








def close(event):
    root.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing

root.bind('<Escape>', close)

root.mainloop() #This is how we run the GUI
