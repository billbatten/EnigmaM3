import tkinter as tk
from tkinter import ttk

def encodeMessage(inputMessage):
    #Original rotor wiring configurations
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
    rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"

    #Original rotor notch configurations
    rotor1Notch = "Q"
    rotor2Notch = "E"
    rotor3Notch = "V"
    rotor4Notch = "J"
    rotor5Notch = "Z"

    reflectorA = {"A":"E","E":"A","B":"J","J":"B","C":"M","M":"C","D":"Z","Z":"D",
                  "F":"L","L":"F","G":"Y","Y":"G","H":"X","X":"H","I":"V","V":"I",
                  "K":"W","W":"K","N":"R","R":"N","O":"Q","Q":"O","P":"U","U":"P",
                  "S":"T","T":"S"}

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"




#Start of program
print("----Enigma M3 Simulation-----\n")
#rotorANum = int(input("Please select which rotor from 1-5 that will go at rotor position A"))
#rotorBNum = int(input("Please select which rotor from 1-5 that will go at rotor position B"))
#rotorCNum = int(input("Please select which rotor from 1-5 that will go at rotor position C"))

#initalRotorA = input("What letter for rotor A would you like to start on? ")
#initalRotorA.upper()
#initalRotorB = input("What letter for rotor A would you like to start on? ")
#initalRotorB.upper()
#initalRotorC = input("What letter for rotor A would you like to start on? ")
#initalRotorC.upper()

#inputMessage = input("Please input a message to encrypt - ")

#encodeMessage("hello")


#GUI Creation
key = tk.Tk()

exp = " "
print(exp)
def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)

print(exp)
key.geometry('1010x250')
key.maxsize(width=600, height=250)
key.minsize(width=600, height=250)

key.configure(bg = 'black')

equation = tk.StringVar()
Dis_entry = ttk.Entry(key,state= 'readonly',textvariable = equation)
Dis_entry.grid(rowspan= 1 , columnspan = 100, ipadx = 200 , ipady = 20)

#TOP ROW KEYBOARD
q = ttk.Button(key,text = 'Q' , width = 6, command = lambda : press('Q'))
q.grid(row = 1 , column = 0, ipadx = 6 , ipady = 10)
w = ttk.Button(key,text = 'W' , width = 6, command = lambda : press('W'))
w.grid(row = 1 , column = 1, ipadx = 6 , ipady = 10)
E = ttk.Button(key,text = 'E' , width = 6, command = lambda : press('E'))
E.grid(row = 1 , column = 2, ipadx = 6 , ipady = 10)
R = ttk.Button(key,text = 'R' , width = 6, command = lambda : press('R'))
R.grid(row = 1 , column = 3, ipadx = 6 , ipady = 10)
T = ttk.Button(key,text = 'T' , width = 6, command = lambda : press('T'))
T.grid(row = 1 , column = 4, ipadx = 6 , ipady = 10)
Y = ttk.Button(key,text = 'Y' , width = 6, command = lambda : press('Y'))
Y.grid(row = 1 , column = 5, ipadx = 6 , ipady = 10)
U = ttk.Button(key,text = 'U' , width = 6, command = lambda : press('U'))
U.grid(row = 1 , column = 6, ipadx = 6 , ipady = 10)
I = ttk.Button(key,text = 'I' , width = 6, command = lambda : press('I'))
I.grid(row = 1 , column = 7, ipadx = 6 , ipady = 10)
O = ttk.Button(key,text = 'O' , width = 6, command = lambda : press('O'))
O.grid(row = 1 , column = 8, ipadx = 6 , ipady = 10)
P = ttk.Button(key,text = 'P' , width = 6, command = lambda : press('P'))
P.grid(row = 1 , column = 9, ipadx = 6 , ipady = 10)


#MIDDLE ROW KEYBOARD
A = ttk.Button(key,text = 'A' , width = 6, command = lambda : press('A'))
A.grid(row = 2, column = 1, ipadx = 6 , ipady = 10)
S = ttk.Button(key,text = 'S' , width = 6, command = lambda : press('S'))
S.grid(row = 2, column = 2, ipadx = 6 , ipady = 10)
D = ttk.Button(key,text = 'D' , width = 6, command = lambda : press('D'))
D.grid(row = 2, column = 3, ipadx = 6 , ipady = 10)
F = ttk.Button(key,text = 'F' , width = 6, command = lambda : press('F'))
F.grid(row = 2, column = 4, ipadx = 6 , ipady = 10)
G = ttk.Button(key,text = 'G' , width = 6, command = lambda : press('G'))
G.grid(row = 2, column = 5, ipadx = 6 , ipady = 10)
H = ttk.Button(key,text = 'H' , width = 6, command = lambda : press('H'))
H.grid(row = 2, column = 6, ipadx = 6 , ipady = 10)
J = ttk.Button(key,text = 'J' , width = 6, command = lambda : press('J'))
J.grid(row = 2, column = 7, ipadx = 6 , ipady = 10)
K = ttk.Button(key,text = 'K' , width = 6, command = lambda : press('K'))
K.grid(row = 2, column = 8, ipadx = 6 , ipady = 10)
L = ttk.Button(key,text = 'L' , width = 6, command = lambda : press('L'))
L.grid(row = 2, column = 9, ipadx = 6 , ipady = 10)


#BOTTOM ROW KEYBOARD
Z = ttk.Button(key,text = 'Z' , width = 6, command = lambda : press('Z'))
Z.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)
X = ttk.Button(key,text = 'X' , width = 6, command = lambda : press('X'))
X.grid(row = 3 , column = 3, ipadx = 6 , ipady = 10)
C = ttk.Button(key,text = 'C' , width = 6, command = lambda : press('C'))
C.grid(row = 3 , column = 4, ipadx = 6 , ipady = 10)
V = ttk.Button(key,text = 'V' , width = 6, command = lambda : press('V'))
V.grid(row = 3 , column = 5, ipadx = 6 , ipady = 10)
B = ttk.Button(key, text= 'B' , width = 6 , command = lambda : press('B'))
B.grid(row = 3 , column = 6 , ipadx = 6 ,ipady = 10)
N = ttk.Button(key,text = 'N' , width = 6, command = lambda : press('N'))
N.grid(row = 3 , column = 7, ipadx = 6 , ipady = 10)
M = ttk.Button(key,text = 'M' , width = 6, command = lambda : press('M'))
M.grid(row = 3 , column = 8, ipadx = 6 , ipady = 10)

space = ttk.Button(key,text = 'Space' , width = 6, command = lambda : press(' '))
space.grid(row = 4 , columnspan = 14 , ipadx = 160 , ipady = 10)


key.mainloop()
