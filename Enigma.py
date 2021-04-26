"""
In order to encrypt/decrypt a message each letter must past through each component in the machine
in a specific order
Keyboard -> plugboard -> rotor 3 -> rotor 2 -> rotor 1 -> reflector -> rotor 1 -> rotor 2 -> rotor 3
plugboard -> lampboard
"""




def alphabetRotation(startLetter):
    #THIS FUNCTION OFFSETS THE ALPHABET TO MATCH THE THE STARTING LETTER

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = alphabet.index(startLetter)
    newAlphabet = alphabet[index:26] + alphabet[:index]
    return newAlphabet

def rotorConfigurationShift(startLetter, rotorConfiguration, offset):

    #THIS IS THE FUNCTION FOR IMPLEMENTATION OF THE RING SETTING ENCRYTPION.
    #THE RING SETTING SHIFTS EACH LETTER OF THE WIRING CONFIGURATION THROUGH THE ALPHABET
    #DEPENDING ON THE RING SETTING. I.E IF RING SETTING = C, EACH LETTER OF THE WIRING
    #CONFIGURATION WOULD BE SHIFTED 2 LETTERS THROUGH THE ALPHABET. ALSO THE CONFIGURATION
    #IS SHIFTED TO ALLIGN WITH STARTING LETTER OF EACH ROTOR

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newConfig = ""

    for i in rotorConfiguration:
        index = alphabet.index(i)
        index = (index + offset) % 26
        shiftedLetter = alphabet[index]
        newConfig = newConfig + shiftedLetter
        newConfigString = newConfig[26 - offset:] + newConfig[0:26 - offset]

    index = alphabet.index(startLetter)
    newRotorConfiguration = newConfigString[index:26] + newConfigString[:index]
    return newRotorConfiguration


def encrypt(inputMessage, rotorSelection, rotorStartPos, plugboardSettings, reflectorSelection, ringSetting):

    removeInputSpaces = inputMessage.replace(" ", "")
    inputMessage = removeInputSpaces

    #English alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Retrieves the wiring configuration for the user selected rotor
    rotorConfiqDict = {"1":"EKMFLGDQVZNTOWYHXUSPAIBRCJ", "2":"AJDKSIRUXBLHWTMCQGZNPYFVOE", "3":"BDFHJLCPRTXVZNYEIWGAKMUSQO",
                       "4":"ESOVPZJAYQUIRHXLNFTGKDCMWB", "5":"VZBRGITYUPSDNHLXAWMJQOFECK"}


    UKWB = {"A":"Y", "Y":"A", "B":"R", "R":"B", "C":"U", "U":"C", "D":"H", "H":"D", "E":"Q", "Q":"E", "F":"S", "S":"F",
            "G":"L", "L":"G", "I":"P", "P":"I", "J":"X", "X":"J", "K":"N", "N":"K", "M":"O", "O":"M", "T":"Z", "Z":"T",
            "V":"W", "W":"V"}
    UKWC = {"A":"F", "F":"A", "B":"V", "V":"B", "C":"P", "P":"C", "D":"J", "J":"D", "E":"I", "I":"E", "G":"O", "O":"G",
            "H":"Y", "Y":"H", "K":"R", "R":"K", "L":"Z", "Z":"L", "M":"X", "X":"M", "N":"W", "W":"N", "Q":"T", "T":"Q",
            "S":"U", "U":"S"}

    if reflectorSelection == "B":
        reflector = UKWB
    if reflectorSelection == "C":
        reflector = UKWC


    #Create a dictionary containing the rotor number and it's notch letter
    notchDict = {"1": "Q", "2": "E", "3": "V", "4": "J", "5": "Z"}

    #ROTOR A NOTCH NOT NECESSARY AS IT DOESNT IMPACT OTHER ROTORS
    rotorBNotch = notchDict.get(rotorSelection[1])
    rotorCNotch = notchDict.get(rotorSelection[2])

    #Variable to store the user selected starting letter
    rotorALetter = rotorStartPos[0]
    rotorBLetter = rotorStartPos[1]
    rotorCLetter = rotorStartPos[2]

    #Empty string that encrypted letter will be added to
    encryptedMessage = ""

    #Make user input message and plugboard pairs uppercase
    inputMessage = inputMessage.upper()

    #Pass message through the plugboard
    #Put user plugboard settings into a list then into a dictionary
    # plugboardSettingsList = plugboardSettings.upper().split()
    plugboardSettingsList = plugboardSettings
    plugboardSettingsDict = dict(plugboardSettingsList)






    #Reverse the original dictionary and add it to a new dictionary
    reversedDict = {x: y for y, x in plugboardSettingsDict.items()}
    updatedPlugboardSettingsDict = dict(list(plugboardSettingsDict.items()) + list(reversedDict.items()))

    tempA = rotorConfiqDict.get(rotorSelection[0])
    tempB = rotorConfiqDict.get(rotorSelection[1])
    tempC = rotorConfiqDict.get(rotorSelection[2])

    ringSettingA = alphabet.index(ringSetting[0])
    ringSettingB = alphabet.index(ringSetting[1])
    ringsettingC = alphabet.index(ringSetting[2])

    startingAAlphabet = alphabetRotation(rotorALetter)
    startingBAlphabet = alphabetRotation(rotorBLetter)
    startingCAlphabet = alphabetRotation(rotorCLetter)

    rotorAConfig = rotorConfigurationShift(rotorALetter, tempA, ringSettingA)
    rotorBConfig = rotorConfigurationShift(rotorBLetter, tempB, ringSettingB)
    rotorCConfig = rotorConfigurationShift(rotorCLetter, tempC, ringsettingC)

    #----------------------------------------------------------------------#

    #Rotating of the rotors
    counter = 0
    rotorATrigger = True
    for letter in inputMessage:
        letter = letter.upper()
        encryptedLetter = letter
        if letter in alphabet:
            if rotorBLetter == rotorBNotch and rotorATrigger == True:
                rotorATrigger = False
                counter = 0

                rotorALetter = (alphabet.index(rotorALetter))
                indexA = (rotorALetter + 1) % 26
                rotorALetter = alphabet[indexA]

                rotorBLetter = (alphabet.index(rotorBLetter))
                indexB = (rotorBLetter + 1) % 26
                rotorBLetter = alphabet[indexB]

            #If the current letter is the notch letter activa te trigger and rotate rotor 1 place
            if rotorCLetter == rotorCNotch:
                rotorBLetter = (alphabet.index(rotorBLetter))
                indexB = (rotorBLetter + 1) % 26
                rotorBLetter = alphabet[indexB]

            rotorCLetter = (alphabet.index(rotorCLetter))
            indexC = (rotorCLetter + 1) % 26
            rotorCLetter = alphabet[indexC]

            counter += 1

            if counter > 25:
                rotorATrigger = True
    #-------------------------------------------------------#

        #Loops through each letter in inputMessage and swaps it with the plugboard allocated letter


        print("---------------START---------------\n")
        print("BEFORE ENTERING PLUGBOARD ", encryptedLetter)

        if encryptedLetter not in updatedPlugboardSettingsDict:
            encryptedLetter = encryptedLetter
        else:
            encryptedLetter = updatedPlugboardSettingsDict[encryptedLetter]


        print("AFTER ENTERING PLUGBOARD ", encryptedLetter, "\n")

        numberOfATurns = startingAAlphabet.index(rotorALetter)
        numberOfBTurns = startingBAlphabet.index(rotorBLetter)
        numberOfCTurns = startingCAlphabet.index(rotorCLetter)

        print("A turns = ", numberOfATurns, "//",
              "B turns = ", numberOfBTurns, "//",
              "C turns = ", numberOfCTurns, "\n")


        alphabetAShift = startingAAlphabet[numberOfATurns:26] + startingAAlphabet[:numberOfATurns]
        alphabetBShift = startingBAlphabet[numberOfBTurns:26] + startingBAlphabet[:numberOfBTurns]
        alphabetCShift = startingCAlphabet[numberOfCTurns:26] + startingCAlphabet[:numberOfCTurns]

        index = alphabet.index(encryptedLetter)
        encryptedLetter = alphabetCShift[index % 26]
        print("Rotor C entry point = ", encryptedLetter)

        #ROTOR C ENCRYPTION
        index = alphabetCShift.index(encryptedLetter)
        scrambledLetter = rotorCConfig[(index + numberOfCTurns) % 26]
        print("Rotor C encrypted letter = ", scrambledLetter, "\n")
        index = alphabetCShift.index(scrambledLetter)
        encryptedLetter = alphabetBShift[index % 26]
        print("Rotor B entry point = ", encryptedLetter)

        #ROTOR B ENCRYPTION
        index = alphabetBShift.index(encryptedLetter)
        scrambledLetter = rotorBConfig[(index + numberOfBTurns) % 26]
        print("Rotor B encrypted letter = ", scrambledLetter, "\n")
        index = alphabetBShift.index(scrambledLetter)
        encryptedLetter = alphabetAShift[index % 26]
        print("Rotor A entry point = ", encryptedLetter)

        #ROTOR A ENCRYPTION
        index = alphabetAShift.index(encryptedLetter)
        scrambledLetter = rotorAConfig[(index + numberOfATurns) % 26]
        print("Rotor A encrypted letter = ", scrambledLetter, "\n")
        index = alphabetAShift.index(scrambledLetter)
        encryptedLetter = alphabet[index % 26]
        print("Reflector entry point = ", encryptedLetter)

        #REFLECTOR ENCRYPTION
        if encryptedLetter in reflector:
            encryptedLetter = reflector[encryptedLetter]
        print("Reflector exit point = ", encryptedLetter, "\n")

        index = alphabet.index(encryptedLetter)
        encryptedLetter = alphabetAShift[index % 26]
        print("Rotor A entry point = ", encryptedLetter)

        #NEW ROTOR A ENCRYPTION
        index = rotorAConfig.index(encryptedLetter)
        scrambledLetter = alphabetAShift[(index - numberOfATurns) % 26]
        print("Rotor A encrypted letter = ", scrambledLetter, "\n")
        index = alphabetAShift.index(scrambledLetter)
        encryptedLetter = alphabetBShift[index % 26]
        print("Rotor B entry point = ", encryptedLetter)

        #ROTOR B UPDATED ENCRYPTION TO COUNTER ROTOR B TRIGGER
        index = rotorBConfig.index(encryptedLetter)
        scrambledLetter = alphabetBShift[(index - numberOfBTurns) % 26]
        print("Rotor B encrypted letter = ", scrambledLetter, "\n")
        index = alphabetBShift.index(scrambledLetter)
        encryptedLetter = alphabetCShift[index % 26]
        print("Rotor C entry point = ", encryptedLetter)

        #ROTOR C ENCRYPTION
        index = rotorCConfig.index(encryptedLetter)
        scrambledLetter = alphabetCShift[(index - numberOfCTurns) % 26]
        print("Rotor C encrypted letter = ", scrambledLetter, "\n")
        index = alphabetCShift.index(scrambledLetter)
        encryptedLetter = alphabet[index % 26]

        print("Letter passed to plugboard = ", encryptedLetter)

        if encryptedLetter not in updatedPlugboardSettingsDict:
            encryptedLetter = encryptedLetter
        else:
            encryptedLetter = updatedPlugboardSettingsDict[encryptedLetter]

        print("Lampboard output = ", encryptedLetter, "\n")

        encryptedMessage = encryptedMessage + encryptedLetter

        print("encryptedLetter = ", encryptedLetter)
        print("Encrypted message = ", encryptedMessage, "\n")
        print("A=", rotorALetter, "B=", rotorBLetter, "C=", rotorCLetter)
        print("\n----------------END-----------------")


    return encryptedMessage

#USER INPUTS
#inputMessage = input("Message you wish to encrypt - ")
#rotorSelection = input("Please select the rotors you would like at positions ABC - ")
#rotorStartPos = input("Please list the initial starting positions in order of rotor A, B & C - ")
#reflectorSelection = input("Please select which reflector you wish to use - ")
#plugboardSettings = input("Please list your plugboard pairs settings separated by a space. E.g A=B,C=D,E=F - ")

#USER INPUTS
# inputMessage = "IZ"
# #inputMessage = printtext()
# rotorSelection = "253"
# rotorStartPos = "BZT"
# reflectorSelection = "B"
# plugboardSettings = "AS BD CZ UI FG OQ XY"
# ringSetting = "CQR"



#encryptedMessage = encrypt(inputMessage, rotorSelection, rotorStartPos, plugboardSettings, reflectorSelection, ringSetting)