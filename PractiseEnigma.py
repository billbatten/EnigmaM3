#In order to encrypt/decrypt a message each letter must past through each component in the machine
#in a specific order
#Keyboard -> plugboard -> rotor 3 -> rotor 2 -> rotor 1 -> reflector -> rotor 1 -> rotor 2 -> rotor 3
#plugboard -> lampboard

def encrypt(inputMessage, rotorSelection, rotorStartPos, plugboardSettings):

    #English alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
             #ABCDEFGHIJKLMNOPQRSTUVWXYZ
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

    reflectorA = {"A":"E","E":"A","B":"J","J":"B","C":"M","M":"C","D":"Z","Z":"D",
                  "F":"L","L":"F","G":"Y","Y":"G","H":"X","X":"H","I":"V","V":"I",
                  "K":"W","W":"K","N":"R","R":"N","O":"Q","Q":"O","P":"U","U":"P",
                  "S":"T","T":"S"}

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
        if letter in inputMessage:
            encryptedLetter = updatedPlugboardSettingsDict[letter]


        numberOfATurns = alphabet.index(rotorALetter)
        numberOfBTurns = alphabet.index(rotorBLetter)
        numberOfCTurns = alphabet.index(rotorCLetter)


        #ROTOR C ENCRYPTION
        index = alphabet.index(encryptedLetter)
        scrambledLetter = rotorCConfig[(index + numberOfCTurns) % 26]
        index = alphabet.index(scrambledLetter)
        encryptedLetter = alphabet[(index - numberOfCTurns + 26) % 26]
        print("ROTOR C Encrypted Letter = ", encryptedLetter)

        #ROTOR B ENCRYPTION
        index = alphabet.index(encryptedLetter)
        scrambledLetter = rotorBConfig[(index + numberOfBTurns) % 26]
        index = alphabet.index(scrambledLetter)
        encryptedLetter = alphabet[(index - numberOfBTurns + 26) % 26]
        print("ROTOR B Encrypted Letter = ", encryptedLetter)

        #ROTOR A ENCRYPTION
        index = alphabet.index(encryptedLetter)
        scrambledLetter = rotorAConfig[(index + numberOfATurns) % 26]
        index = alphabet.index(scrambledLetter)
        encryptedLetter = alphabet[(index - numberOfATurns + 26) % 26]
        print("ROTOR A Encrypted Letter = ", encryptedLetter)

        if encryptedLetter in reflectorA:
            encryptedLetter = reflectorA[encryptedLetter]
            print("REFLECTOR ", encryptedLetter)

        #ROTOR A ENCRYPTION
        index = alphabet.index(encryptedLetter)
        scrambledLetter = rotorAConfig[(index + numberOfATurns) % 26]
        index = alphabet.index(scrambledLetter)
        encryptedLetter = alphabet[(index - numberOfATurns + 26) % 26]
        print("ROTOR A Encrypted Letter = ", encryptedLetter)

        #ROTOR B ENCRYPTION
        index = alphabet.index(encryptedLetter)
        scrambledLetter = rotorBConfig[(index + numberOfBTurns) % 26]
        index = alphabet.index(scrambledLetter)
        encryptedLetter = alphabet[(index - numberOfBTurns + 26) % 26]
        print("ROTOR B Encrypted Letter = ", encryptedLetter)

        index = alphabet.index(encryptedLetter)
        scrambledLetter = rotorCConfig[(index + numberOfCTurns) % 26]
        index = alphabet.index(scrambledLetter)
        encryptedLetter = alphabet[(index - numberOfCTurns + 26) % 26]
        print("ROTOR C Encrypted Letter = ", encryptedLetter)

        if encryptedLetter in updatedPlugboardSettingsDict:
            encryptedLetter = updatedPlugboardSettingsDict[encryptedLetter]
            print("LAMPBOARD OUTPUT = ", encryptedLetter)







        print("A=", rotorALetter, "B=", rotorBLetter,"C=", rotorCLetter)



    return encryptedMessage



#USER INPUTS
inputMessage = input("Message you wish to encrypt - ")
rotorSelection = input("Please select the rotors you would like at positions ABC - ")
rotorStartPos = input("Please list the initial starting positions in order of rotor A, B & C - ")
rotorStartPos = rotorStartPos.upper()
plugboardSettings = input("Please list your plugboard pairs settings separated by a space. E.g A=B,C=D,E=F - ")

encryptedMessage = encrypt(inputMessage, rotorSelection, rotorStartPos, plugboardSettings)