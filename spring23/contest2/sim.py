# Input: Some string containing alphanumeric text, plus special characters:
# ] : Move cursor to end of string ->
# [ : Move cursor to front of string <-
# < : Backspace

numCases = int(input())

for i in range(numCases):
    caseInput = input()
    remainsToParse = caseInput
    outString = ""
    addToEnd = True
    EOL = False

    # Find earliest special character
    foundPos = None
    while True:
        
        # Check for pos of end of this block
        foundPos = min([x for x in [remainsToParse.find('['), remainsToParse.find(']'), 1000000] if x != -1])

        if foundPos == 1000000:
            EOL = True
            foundPos = len(remainsToParse)
        
        # Backspace added section



        # Add until next special char reached
        if addToEnd == True:
            outString = outString + remainsToParse[:foundPos]
        else:
            outString = remainsToParse[:foundPos] + outString

        if EOL:
            break
        # Change add mode 
        if remainsToParse[foundPos] == '[':
            addToEnd = False
        elif remainsToParse[foundPos] == ']':
            addToEnd = True

        fullStr = outString
        while True:
            if fullStr[0] == '<':
                fullStr = fullStr[1:]
            else:
                break
        outString = fullStr

        remainsToParse = remainsToParse[foundPos+1:]

        # Remove ineffective backspaces from next segment
        if addToEnd == False:
            fullStr = remainsToParse
            while True:
                if fullStr[0] == '<':
                    fullStr = fullStr[1:]
                else:
                    break
            remainsToParse = fullStr

    # Remove backspaced
    while True:
        foundPos = outString.find("<")
        if not foundPos == -1:
            outString = outString[:foundPos-1] + outString[foundPos+1:]
        else:
            break
        

    print(outString)


