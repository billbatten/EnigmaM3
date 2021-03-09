str = input("Input string - ")
amount = 1
output = ""
for i in range(0, len(str)):
    c = str[i]
    code = ord(c)
    if ((code >= 65) and (code <= 90)):
        c = chr(((code - 65 + amount) % 26) + 65)
    output = output + c
    print("output = ", output)