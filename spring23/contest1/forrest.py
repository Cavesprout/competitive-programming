mode, inStr = input().split()

outStr = ""


strLen = len(inStr)
if mode == "D":
    charScan = 0
    while (charScan < strLen):
        if ord(inStr[charScan]) > 48 and ord(inStr[charScan]) < 58:
            for i in range(int(inStr[charScan])):
                outStr += inStr[charScan-1]
        charScan += 1
elif mode == "E":
    numChar = 1
    charScan = 1
    while (charScan < strLen):
        if (inStr[charScan] == inStr[charScan - 1]):
            numChar += 1
        else:
            outStr += inStr[charScan - 1]
            outStr += str(numChar)
            numChar = 1
        charScan += 1

    outStr += inStr[charScan - 1]
    outStr += str(numChar)

print(outStr)






def checkNumIs10(inNum):
    return inNum == 10

if checkNumIs10(10):
    print("yes")


if 10 == 10:
    print("yes")