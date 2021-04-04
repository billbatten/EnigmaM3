#In order to encrypt/decrypt a message each letter must past through each component in the machine
#in a specific order
#Keyboard -> plugboard -> rotor 3 -> rotor 2 -> rotor 1 -> reflector -> rotor 1 -> rotor 2 -> rotor 3
#plugboard -> lampboard

def alphabetRotation(startLetter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = alphabet.index(startLetter)
    newAlphabet = alphabet[index:26] + alphabet[:index]
    return newAlphabet

def rotorConfigurationShift(startLetter, rotorConfiguration):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = alphabet.index(startLetter)
    newRotorConfiguration = rotorConfiguration[index:26] + rotorConfiguration[:index]
    return newRotorConfiguration

def encrypt(inputMessage, rotorSelection, rotorStartPos, plugboardSettings):

    removeInputSpaces = inputMessage.replace(" ","")
    print("removeInputSpaces = ", removeInputSpaces)
    inputMessage = removeInputSpaces
    print(removeInputSpaces)

    #English alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    rotorARingSetting = "A"
    rotorBRingSetting = "A"
    rotorCRingSetting = "A"

    #NEEDS IMPLEMENTING STILL ^



    #Original rotor wiring configurations
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
    rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"

    #Retrieves the wiring configuration for the user selected rotor
    rotorConfiqDict = {"1":"EKMFLGDQVZNTOWYHXUSPAIBRCJ", "2":"AJDKSIRUXBLHWTMCQGZNPYFVOE", "3":"BDFHJLCPRTXVZNYEIWGAKMUSQO",
                       "4":"ESOVPZJAYQUIRHXLNFTGKDCMWB", "5":"VZBRGITYUPSDNHLXAWMJQOFECK"}

    #Original rotor notch configurations
    rotor1Notch = "Q"
    rotor2Notch = "E"
    rotor3Notch = "V"
    rotor4Notch = "J"
    rotor5Notch = "Z"

    UKWB = {"A":"Y", "Y":"A", "B":"R", "R":"B", "C":"U", "U":"C", "D":"H", "H":"D", "E":"Q", "Q":"E", "F":"S", "S":"F",
            "G":"L", "L":"G", "I":"P", "P":"I", "J":"X", "X":"J", "K":"N", "N":"K", "M":"O", "O":"M", "T":"Z", "Z":"T",
            "V":"W", "W":"V"}

    #Set rotors to user inputs
    rotorA = rotorSelection[0]
    rotorB = rotorSelection[1]
    rotorC = rotorSelection[2]

    #Variable to retrieve the configuration string for the user selected rotor
    rotorAConfig = rotorConfiqDict.get(rotorSelection[0])
    rotorBConfig = rotorConfiqDict.get(rotorSelection[1])
    rotorCConfig = rotorConfiqDict.get(rotorSelection[2])

    #Create a dictionary containing the rotor number and it's notch letter
    notchDict = {"1": "Q", "2": "E", "3": "V", "4": "J", "5": "Z"}

    rotorANotch = notchDict.get(rotorSelection[0])
    rotorBNotch = notchDict.get(rotorSelection[1])
    rotorCNotch = notchDict.get(rotorSelection[2])

    #Variable to store the user selected starting letter
    rotorALetter = rotorStartPos[0]
    rotorBLetter = rotorStartPos[1]
    rotorCLetter = rotorStartPos[2]

    #Empty string that encrypted letter will be added to
    encryptedMessage = ""
    encryptedLetter = ""

    #Make user input message and plugboard pairs uppercase
    inputMessage = inputMessage.upper()

    #Pass message through the plugboard
    #Put user plugboard settings into a list then into a dictionary
    plugboardSettingsList = plugboardSettings.upper().split()
    plugboardSettingsDict = dict(plugboardSettingsList)

    #Reverse the original dictionary and add it to a new dictionary
    reversedDict = {x: y for y, x in plugboardSettingsDict.items()}
    updatedPlugboardSettingsDict = dict(list(plugboardSettingsDict.items()) + list(reversedDict.items()))

    tempA = rotorConfiqDict.get(rotorSelection[0])
    tempB = rotorConfiqDict.get(rotorSelection[1])
    tempC = rotorConfiqDict.get(rotorSelection[2])

    startingAAlphabet = alphabetRotation(rotorALetter)
    startingBAlphabet = alphabetRotation(rotorBLetter)
    startingCAlphabet = alphabetRotation(rotorCLetter)

    rotorAConfig = rotorConfigurationShift(rotorALetter, tempA)
    rotorBConfig = rotorConfigurationShift(rotorBLetter, tempB)
    rotorCConfig = rotorConfigurationShift(rotorCLetter, tempC)

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

            #If the current letter is the notch letter activate trigger and rotate rotor 1 place
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


        # startingAAlphabet = alphabetStart(rotorALetter)
        # startingBAlphabet = alphabetStart(rotorBLetter)
        # startingCAlphabet = alphabetStart(rotorCLetter)
        # print("TEST ALPHABET CODE - ", startingAAlphabet)
        # print("TEST ALPHABET CODE - ", startingBAlphabet)
        # print("TEST ALPHABET CODE - ", startingCAlphabet)

        numberOfATurns = startingAAlphabet.index(rotorALetter)
        numberOfBTurns = startingBAlphabet.index(rotorBLetter)
        numberOfCTurns = startingCAlphabet.index(rotorCLetter)

        # numberOfATurns = alphabet.index(rotorALetter)
        # numberOfBTurns = alphabet.index(rotorBLetter)
        # numberOfCTurns = alphabet.index(rotorCLetter)
        print("A turns = ", numberOfATurns, "//",
              "B turns = ", numberOfBTurns, "//",
              "C turns = ", numberOfCTurns, "\n")




        # tempA = rotorConfiqDict.get(rotorSelection[0])
        # tempB = rotorConfiqDict.get(rotorSelection[1])
        # tempC = rotorConfiqDict.get(rotorSelection[2])

        # if numberOfATurns > 0:
        #     rotorAConfig = tempA[26 - numberOfATurns:] + tempA[0:26 - numberOfATurns]
        # if numberOfBTurns > 0:
        #     rotorBConfig = tempB[26 - numberOfBTurns:] + tempB[0:26 - numberOfBTurns]
        # if numberOfCTurns > 0:
        #     rotorCConfig = tempC[26 - numberOfCTurns:] + tempC[0:26 - numberOfCTurns]
        #     #rotorCConfig = tempC[numberOfCTurns:26] + tempC[:numberOfCTurns]

        # alphabetAShift = alphabet[numberOfATurns:26] + alphabet[:numberOfATurns]
        # alphabetBShift = alphabet[numberOfBTurns:26] + alphabet[:numberOfBTurns]
        # alphabetCShift = alphabet[numberOfCTurns:26] + alphabet[:numberOfCTurns]

        alphabetAShift = startingAAlphabet[numberOfATurns:26] + startingAAlphabet[:numberOfATurns]
        alphabetBShift = startingBAlphabet[numberOfBTurns:26] + startingBAlphabet[:numberOfBTurns]
        alphabetCShift = startingCAlphabet[numberOfCTurns:26] + startingCAlphabet[:numberOfCTurns]

        # rotorAConfig = tempA[numberOfATurns:26] + tempA[:numberOfATurns]
        # rotorBConfig = tempB[numberOfBTurns:26] + tempB[:numberOfBTurns]
        # rotorCConfig = tempC[numberOfCTurns:26] + tempC[:numberOfCTurns]

        # print(alphabet)
        # print(alphabetCShift)
        # print(rotorCConfig)

        index = alphabet.index(encryptedLetter)


        #rotorCEntryPoint1 = alphabetCShift[index % 26]
        encryptedLetter = alphabetCShift[index % 26]
        print("Rotor C entry point = ", encryptedLetter)

        # THIS SECTION NEEDS FIXING ^^^

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
        encryptedLetter = alphabet[index]


        #REFLECTOR ENCRYPTION
        print("Reflector entry point = ", encryptedLetter)
        if encryptedLetter in UKWB:
            encryptedLetter = UKWB[encryptedLetter]
        print("Reflector exit point = ", encryptedLetter, "\n")

        index = alphabet.index(encryptedLetter)
        encryptedLetter = alphabetAShift[(index + numberOfATurns) % 26]
        print("Rotor A entry point = ", encryptedLetter)

        #NEW ROTOR A ENCRYPTION
        index = rotorAConfig.index(encryptedLetter)
        scrambledLetter = alphabetAShift[(index - numberOfATurns) % 26]
        print("Rotor A encrypted letter = ", scrambledLetter, "\n")
        index = alphabetAShift.index(scrambledLetter)
        encryptedLetter = alphabetBShift[index % 26]
        print("Rotor B entry point = ", encryptedLetter)


        #ROTOR A ENCRYPTION
        # index = rotorAConfig.index(encryptedLetter) #13
        # scrambledLetter = alphabetAShift[(index + numberOfATurns) % 26]  #alphabetAShift[13] = N
        # print("Rotor A encrypted letter = ", scrambledLetter, "\n")
        # index = rotorAConfig.index(scrambledLetter) #10
        # encryptedLetter = rotorAConfig[(index - numberOfATurns + 26) % 26] #N
        # index = alphabetBShift.index(encryptedLetter) #12
        # rotorBEntry2 = alphabetBShift[(index + numberOfBTurns) % 26]
        # #print("Rotor B entry point = ", alphabetBShift[index + numberOfBTurns])
        # print("Rotor B entry point ", rotorBEntry2) #O


        #ROTOR B UPDATED ENCRYPTION TO COUNTER ROTOR B TRIGGER
        index = rotorBConfig.index(encryptedLetter)
        scrambledLetter = alphabetBShift[(index - numberOfBTurns) % 26]
        print("Rotor B encrypted letter = ", scrambledLetter, "\n")
        index = alphabetBShift.index(scrambledLetter)
        encryptedLetter = alphabetCShift[index]
        print("Rotor C entry point = ", encryptedLetter)


        #ROTOR B ENCRYPTION
        # index = rotorBConfig.index(encryptedLetter) #18 #23
        # scrambledLetter = alphabetBShift[(index + numberOfBTurns) % 26]
        # print("Rotor B encrypted letter = ", scrambledLetter, "\n")
        # index = rotorBConfig.index(scrambledLetter)
        # encryptedLetter = rotorBConfig[(index - numberOfBTurns + 26) % 26]
        # index = alphabetBShift.index(encryptedLetter)
        # encryptedLetter = alphabetCShift[index]
        # print("Rotor C entry point = ", encryptedLetter)


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
#inputMessage = "abcdefghijklmnopqrstuvwxyzabc"
inputMessage = "abc"
#inputMessage = "hello"


#rotorSelection = input("Please select the rotors you would like at positions ABC - ")
rotorSelection = "123"

#rotorStartPos = input("Please list the initial starting positions in order of rotor A, B & C - ")
#rotorStartPos = rotorStartPos.upper()
#rotorStartPos = "AAA"
rotorStartPos = "PDU"

#plugboardSettings = input("Please list your plugboard pairs settings separated by a space. E.g A=B,C=D,E=F - ")
plugboardSettings = "AS BD CZ UI"

encryptedMessage = encrypt(inputMessage, rotorSelection, rotorStartPos, plugboardSettings)