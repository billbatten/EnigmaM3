import tkinter as tk
from tkinter import ttk
import time
from tkinter import *


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

print("-Plain Text-")


