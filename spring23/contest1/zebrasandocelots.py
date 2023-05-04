


numLines = int(input())



stack = ""
for i in range(numLines):
    stack += input()

rings = 0

lowestOcelotPos = -1

while ("O" in stack):
    lowestOcelotPos = stack.rfind("O")
    prunedStr = stack[:lowestOcelotPos]
    prunedStr += "Z"
    prunedStr += ("O") * (numLines - len(prunedStr))
    print(prunedStr + " " + str(lowestOcelotPos))
    stack = prunedStr
    rings += 1

print(rings)