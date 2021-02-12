from tkinter import *
import tkinter as tk

keyboard = tk.Tk()
keyboard.title("HELLO")
keyboard.attributes("-fullscreen", True)

keyboard.configure(bg = "black")


spaceBar = Button(keyboard, text='SPACE', width=40, height=3)
spaceBar.pack(side = BOTTOM, pady = 20)

button = CustomButton(keyboard, 100, 25, 'red')
button.pack()

Q = Button(keyboard, text='Q', width=6, height= 3)
Q.place(x = 500, y = 800)

W = Button(keyboard, text='W', width=6, height= 3)
W.place(x = 555, y = 800)

Q = Button(keyboard, text='E', width=6, height= 3, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
Q.place(x = 610, y = 800)

R = Button(keyboard, text='R', width=6, height= 3, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
R.place(x = 665, y = 800)

T = Button(keyboard, text='T', width=6, height= 3, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
T.place(x = 720, y = 800)

Y = Button(keyboard, text='Y', width=6, height= 3, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
Y.place(x = 775, y = 800)

U = Button(keyboard, text='U', width=6, height= 3, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
U.place(x = 830, y = 800)

E = Button(keyboard, text='R', width=6, height= 3, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
E.place(x = 665, y = 800)

keyboard.mainloop()
# #GUI Creation
# key = tk.Tk()
# exp = ""
#
#
# def press(num):
#     global exp
#     exp = exp + str(num)
#     equation.set(exp)
#     print("\r", exp, end="")
#     time.sleep(0.25)
#
#
# width= key.winfo_screenwidth()
# height= key.winfo_screenheight()
# print(width)
# print(height)
# key.geometry("%dx%d" % (width, height))
#
# key.configure(bg = 'black')
#
# equation = tk.StringVar()
# Dis_entry = ttk.Entry(key,state= 'readonly',textvariable = equation)
# Dis_entry.grid(rowspan= 10 , columnspan = 100, ipadx = 10 , ipady = 20)
#
# #TOP ROW KEYBOARD
# Q = ttk.Button(key,text = 'Q' , width = 6, command = lambda : press('Q'))
# Q.grid(row = 150, column = 1000, ipadx = 6 , ipady = 10)
# W = ttk.Button(key,text = 'W' , width = 6, command = lambda : press('W'))
# W.grid(row = 1 , column = 1, ipadx = 6 , ipady = 10)
# E = ttk.Button(key,text = 'E' , width = 6, command = lambda : press('E'))
# E.grid(row = 1 , column = 2, ipadx = 6 , ipady = 10)
# R = ttk.Button(key,text = 'R' , width = 6, command = lambda : press('R'))
# R.grid(row = 1 , column = 3, ipadx = 6 , ipady = 10)
# T = ttk.Button(key,text = 'T' , width = 6, command = lambda : press('T'))
# T.grid(row = 1 , column = 4, ipadx = 6 , ipady = 10)
# Y = ttk.Button(key,text = 'Y' , width = 6, command = lambda : press('Y'))
# Y.grid(row = 1 , column = 5, ipadx = 6 , ipady = 10)
# U = ttk.Button(key,text = 'U' , width = 6, command = lambda : press('U'))
# U.grid(row = 1 , column = 6, ipadx = 6 , ipady = 10)
# I = ttk.Button(key,text = 'I' , width = 6, command = lambda : press('I'))
# I.grid(row = 1 , column = 7, ipadx = 6 , ipady = 10)
# O = ttk.Button(key,text = 'O' , width = 6, command = lambda : press('O'))
# O.grid(row = 1 , column = 8, ipadx = 6 , ipady = 10)
# P = ttk.Button(key,text = 'P' , width = 6, command = lambda : press('P'))
# P.grid(row = 1 , column = 9, ipadx = 6 , ipady = 10)
#
#
# #MIDDLE ROW KEYBOARD
# A = ttk.Button(key,text = 'A' , width = 6, command = lambda : press('A'))
# A.grid(row = 2, column = 1, ipadx = 6 , ipady = 10)
# S = ttk.Button(key,text = 'S' , width = 6, command = lambda : press('S'))
# S.grid(row = 2, column = 2, ipadx = 6 , ipady = 10)
# D = ttk.Button(key,text = 'D' , width = 6, command = lambda : press('D'))
# D.grid(row = 2, column = 3, ipadx = 6 , ipady = 10)
# F = ttk.Button(key,text = 'F' , width = 6, command = lambda : press('F'))
# F.grid(row = 2, column = 4, ipadx = 6 , ipady = 10)
# G = ttk.Button(key,text = 'G' , width = 6, command = lambda : press('G'))
# G.grid(row = 2, column = 5, ipadx = 6 , ipady = 10)
# H = ttk.Button(key,text = 'H' , width = 6, command = lambda : press('H'))
# H.grid(row = 2, column = 6, ipadx = 6 , ipady = 10)
# J = ttk.Button(key,text = 'J' , width = 6, command = lambda : press('J'))
# J.grid(row = 2, column = 7, ipadx = 6 , ipady = 10)
# K = ttk.Button(key,text = 'K' , width = 6, command = lambda : press('K'))
# K.grid(row = 2, column = 8, ipadx = 6 , ipady = 10)
# L = ttk.Button(key,text = 'L' , width = 6, command = lambda : press('L'))
# L.grid(row = 2, column = 9, ipadx = 6 , ipady = 10)
#
#
# #BOTTOM ROW KEYBOARD
# Z = ttk.Button(key,text = 'Z' , width = 6, command = lambda : press('Z'))
# Z.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)
# X = ttk.Button(key,text = 'X' , width = 6, command = lambda : press('X'))
# X.grid(row = 3 , column = 3, ipadx = 6 , ipady = 10)
# C = ttk.Button(key,text = 'C' , width = 6, command = lambda : press('C'))
# C.grid(row = 3 , column = 4, ipadx = 6 , ipady = 10)
# V = ttk.Button(key,text = 'V' , width = 6, command = lambda : press('V'))
# V.grid(row = 3 , column = 5, ipadx = 6 , ipady = 10)
# B = ttk.Button(key, text= 'B' , width = 6 , command = lambda : press('B'))
# B.grid(row = 3 , column = 6 , ipadx = 6 ,ipady = 10)
# N = ttk.Button(key,text = 'N' , width = 6, command = lambda : press('N'))
# N.grid(row = 3 , column = 7, ipadx = 6 , ipady = 10)
# M = ttk.Button(key,text = 'M' , width = 6, command = lambda : press('M'))
# M.grid(row = 3 , column = 8, ipadx = 6 , ipady = 10)
#
# space = ttk.Button(key,text = 'Space' , width = 6, command = lambda : press(' '))
# space.grid(row = 4 , columnspan = 14 , ipadx = 160 , ipady = 10)
#
#
# key.mainloop()