#In order to encrypt/decrypt a message each letter must past through each component in the machine
#in a specific order
#Keyboard -> plugboard -> rotor 3 -> rotor 2 -> rotor 1 -> reflector -> rotor 1 -> rotor 2 -> rotor 3
#plugboard -> lampboard

def encrypt(inputMessage, rotorSelection, rotorStartPos, plugboardSettings):

    #English alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
              #"BCDEFGHIJKLMNOPQRSTUVWXYZA"
              #"DFHJLCPRTXVZNYEIWGAKMUSQOB"
              #"QOBDFHJLCPRTXVZNYEIWGAKMUS"
    rotorARingSetting = "A"
    rotorBRingSetting = "A"
    rotorCRingSetting = "A"

    #Original rotor wiring configurations
             #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
             #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
             #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
            #"DFHJLCPRTXVZNYEIWGAKMUSQOB"
            #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
             #ABCDEFGHIJKLMNOPQRSTUVWXYZ
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
    notchDict = {"1":"Q", "2":"E", "3":"V", "4":"J", "5":"Z"}

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
    #plugboardSettings.upper()

    #Pass message through the plugboard
    #Put user plugboard settings into a list then into a dictionary
    plugboardSettingsList = plugboardSettings.upper().split()
    plugboardSettingsDict = dict(plugboardSettingsList)

    #Reverse the original dictionary and add it to a new dictionary
    reversedDict = {x: y for y, x in plugboardSettingsDict.items()}
    updatedPlugboardSettingsDict = dict(list(plugboardSettingsDict.items()) + list(reversedDict.items()))

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

        if encryptedLetter not in updatedPlugboardSettingsDict:
            encryptedLetter = encryptedLetter
        else:
            encryptedLetter = updatedPlugboardSettingsDict[encryptedLetter]


        print("AFTER ENTERING PLUGBOARD ", encryptedLetter)

        numberOfATurns = alphabet.index(rotorALetter)
        print(numberOfATurns)
        numberOfBTurns = alphabet.index(rotorBLetter)
        print(numberOfBTurns)
        numberOfCTurns = alphabet.index(rotorCLetter)
        print(numberOfCTurns)




        tempA = rotorConfiqDict.get(rotorSelection[0])
        tempB = rotorConfiqDict.get(rotorSelection[1])
        tempC = rotorConfiqDict.get(rotorSelection[2])

        # if numberOfATurns > 0:
        #     rotorAConfig = tempA[26 - numberOfATurns:] + tempA[0:26 - numberOfATurns]
        # if numberOfBTurns > 0:
        #     rotorBConfig = tempB[26 - numberOfBTurns:] + tempB[0:26 - numberOfBTurns]
        # if numberOfCTurns > 0:
        #     rotorCConfig = tempC[26 - numberOfCTurns:] + tempC[0:26 - numberOfCTurns]
        #     #rotorCConfig = tempC[numberOfCTurns:26] + tempC[:numberOfCTurns]

        alphabetAShift = alphabet[numberOfATurns:26] + alphabet[:numberOfATurns]
        alphabetBShift = alphabet[numberOfBTurns:26] + alphabet[:numberOfBTurns]
        alphabetCShift = alphabet[numberOfCTurns:26] + alphabet[:numberOfCTurns]




        rotorAConfig = tempA[numberOfATurns:26] + tempA[:numberOfATurns]
        rotorBConfig = tempB[numberOfBTurns:26] + tempB[:numberOfBTurns]
        rotorCConfig = tempC[numberOfCTurns:26] + tempC[:numberOfCTurns]


        # print(alphabet)
        # print(alphabetCShift)
        # print(rotorCConfig)

        index = alphabetCShift.index(encryptedLetter)
        rotorCEntryPoint1 = alphabetCShift[index]
        print("Rotor C entry point = ", rotorCEntryPoint1)

        # THIS SECTION NEEDS FIXING ^^^

        #ROTOR C ENCRYPTION
        index = alphabetCShift.index(encryptedLetter)
        scrambledLetter = rotorCConfig[(index + numberOfCTurns) % 26]
        print("Scrambled Letter = ", scrambledLetter)
        index = alphabet.index(scrambledLetter)
        encryptedLetter = alphabet[(index - numberOfCTurns + 26) % 26]
        rotorBEntryPoint = alphabetBShift[(index - numberOfCTurns + 26) % 26]
        print("ROTOR B entry point = ", rotorBEntryPoint)


        #ROTOR B ENCRYPTION
        index = alphabetBShift.index(encryptedLetter)
        scrambledLetter = rotorBConfig[(index + numberOfBTurns) % 26]
        print("Scrambled Letter = ", scrambledLetter)
        index = alphabet.index(scrambledLetter)
        encryptedLetter = alphabet[(index - numberOfBTurns + 26) % 26]
        print("ROTOR A entry point = ", encryptedLetter)


        #ROTOR A ENCRYPTION
        index = alphabetAShift.index(encryptedLetter)
        scrambledLetter = rotorAConfig[(index + numberOfATurns) % 26]
        print("Scrambled Letter = ", scrambledLetter)
        index = alphabet.index(scrambledLetter)
        encryptedLetter = alphabet[(index - numberOfATurns + 26) % 26]



        #REFLECTOR ENCRYPTION
        print("Reflector entry point = ", encryptedLetter)
        if encryptedLetter in UKWB:
            encryptedLetter = UKWB[encryptedLetter]
            print("\nREFLECTOR ", encryptedLetter, "\n")
        print("Reflector exit point ", encryptedLetter)

        index = alphabetAShift.index(encryptedLetter)
        rotorAEntry2 = alphabetAShift[index + numberOfATurns]
        #print("Rotor A entry point ", alphabetAShift[index + numberOfATurns])
        print("Rotor A entry point ", rotorAEntry2)

        #ROTOR A ENCRYPTION
        index = rotorAConfig.index(encryptedLetter) #13
        scrambledLetter = alphabetAShift[(index + numberOfATurns) % 26]  #alphabetAShift[13] = N
        print("Scrambled LETTER === ", scrambledLetter)
        index = rotorAConfig.index(scrambledLetter) #10
        encryptedLetter = rotorAConfig[(index - numberOfATurns + 26) % 26] #N
        index = alphabetBShift.index(encryptedLetter) #12
        rotorBEntry2 = alphabetBShift[index + numberOfBTurns]
        print("Rotor B entry point ", alphabetBShift[index + numberOfBTurns])
        #print("Rotor B entry point ", rotorBEntry2) #O
        encryptedLetter = rotorBEntry2


        #ROTOR B ENCRYPTION
        index = rotorBConfig.index(encryptedLetter) #18 #23
        scrambledLetter = alphabetBShift[(index + numberOfBTurns) % 26]
        print(print("Scrambled LETTER = ", scrambledLetter))
        index = rotorBConfig.index(scrambledLetter)
        encryptedLetter = rotorBConfig[(index - numberOfBTurns + 26) % 26]
        index = alphabetBShift.index(encryptedLetter)
        encryptedLetter = alphabetCShift[index]
        print("Rotor C entry point ", encryptedLetter)


        #ROTOR C ENCRYPTION
        index = rotorCConfig.index(encryptedLetter)
        scrambledLetter = alphabetCShift[(index + numberOfCTurns) % 26]
        print("Scrambled LETTER!! = ", scrambledLetter)
        #index = rotorCConfig.index(scrambledLetter)
        encryptedLetter = alphabetCShift[(index - numberOfCTurns + 26) % 26]
        print("Letter passed to plugboard ", encryptedLetter)


        if encryptedLetter not in updatedPlugboardSettingsDict:
            encryptedLetter = encryptedLetter
        else:
            encryptedLetter = updatedPlugboardSettingsDict[encryptedLetter]

        print("LAMPBOARD OUTPUT = ", encryptedLetter)

        encryptedMessage = encryptedMessage + encryptedLetter
        print(encryptedMessage, "\n")

        print("A=", rotorALetter, "B=", rotorBLetter, "C=", rotorCLetter)

    return encryptedMessage



#USER INPUTS
#inputMessage = input("Message you wish to encrypt - ")
inputMessage = "abcdefghijklmnopqrstuv"
#inputMessage = "a"
#rotorSelection = input("Please select the rotors you would like at positions ABC - ")
rotorSelection = "123"
#rotorStartPos = input("Please list the initial starting positions in order of rotor A, B & C - ")
#rotorStartPos = rotorStartPos.upper()
rotorStartPos = "AAA"
#plugboardSettings = input("Please list your plugboard pairs settings separated by a space. E.g A=B,C=D,E=F - ")
plugboardSettings = "AS BD CZ UI"

encryptedMessage = encrypt(inputMessage, rotorSelection, rotorStartPos, plugboardSettings)