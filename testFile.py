# str = input("Input string - ")
# amount = 1
# output = ""
# for i in range(0, len(str)):
#     c = str[i]
#     code = ord(c)
#     if ((code >= 65) and (code <= 90)):
#         c = chr(((code - 65 + amount) % 26) + 65)
#     output = output + c
#     print("output = ", output)

# for rotorALetter in rotorA:
#
#     for rotorBLetter in rotorB:
#
#          for rotorCLetter in alphabet:
#              rotorCLetter = (alphabet.index(rotorBLetter))
#              indexC = (rotorBLetter + 1) % 26
#              rotorCLetter = alphabet[indexC]
#              print("A = ", rotorALetter,"B = ", rotorBLetter,"C = ", rotorCLetter)
#             #increment rotor C
#             #END C LOOP
#         #Increment Rotor B
#         #END B LOOP
#     #Increment rotor A
#     #END A LOOP

x = 19%26
print(x)