

def encrypt(inputMessage, rotorSelection, rotorStartPos, plugboardSettings):

    #English alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

    #Set rotors to user inputs
    rotorA = rotorSelection[0]
    rotorB = rotorSelection[1]
    rotorC = rotorSelection[2]

    #Create a dictionary containing the rotor number and it's notch letter
    rotorNotchDict = {"1":"Q", "2":"E", "3":"V", "4":"J", "5":"Z"}

    rotorANotch = rotorNotchDict.get(rotorSelection[0])
    rotorBNotch = rotorNotchDict.get(rotorSelection[1])
    rotorCNotch = rotorNotchDict.get(rotorSelection[2])

    rotorALetter = rotorStartPos[0]
    rotorBLetter = rotorStartPos[1]
    rotorCLetter = rotorStartPos[2]

    encryptedMessage = ""

    #Make user input message and plugboard pairs uppercase
    inputMessage.upper()
    plugboardSettings.upper()

    #Put user plugboard settings into a list then into a dictionary
    plugboardSettingsList = plugboardSettings.split()
    plugboardSettingsDict = dict(plugboardSettingsList)






    return encryptedMessage



inputMessage = input("Message you wish to encrypt - ")
rotorSelection = input("Please select the rotors you would like at positions ABC - ")
rotorStartPos = input("Please list the inital starting positions in order of rotor A, B & C - ")
plugboardSettings = input("Please list your plugboard pairs settings seperated by a space. E.g A=B,C=D,E=F - ")

#How to print a specific pair
#print(plugboardSettings.split(" ")[0])


encryptedMessage = encrypt(inputMessage, rotorSelection, rotorStartPos, plugboardSettings)
