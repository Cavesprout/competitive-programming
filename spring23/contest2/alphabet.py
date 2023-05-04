# Input = a single string with only lowercase letters

# xyzabcdefghijklmnopqrstuvw




# Abandoned recursive approach
# inStr = input()

# def find_alphabet(textString, findChar):
#     print(textString)
#     print("looking for " + findChar)
#     # Base Case
#     if findChar == chr(ord('z') + 1):
#         return 100000000


#     # Recursive Case
#     remainingString = textString
#     foundPos = 0
#     caseCount = 1000000000
#     while foundPos != -1:
#         foundPos = remainingString.find(findChar)
#         caseCount = min(find_alphabet(remainingString[foundPos:], chr(ord(findChar) + 1)), caseCount)
#         remainingString = remainingString[foundPos:]
        
#    return caseCount





# print(find_alphabet(, 'a'))


# New Strategy:
# Create complete graph between all characters, (cost) of each is number of characters needed to add to reach that point.


inStr = "xyzabcdefghijklmnopqrstuvw"
alphabet = [chr(i) for i in range(97, 123)]
paths = {}

# remainingString = inStr
# # Create graph
# for i, letter in enumerate(alphabet):
#     nextChar = chr(ord(letter) + 1)
#     paths[letter] = [(nextChar, 1, remainingString[i:])]
    
#     foundPos = None
#     while foundPos != -1:
#         foundPos = remainingString.find(nextChar)
#         remainingString = remainingString[foundPos+1:]
#         if foundPos != -1:
#             paths[letter].append((nextChar, 0, remainingString))
#     print("Searched for", nextChar, "in", remainingString)

# for key in paths:
#     print(paths[key])

# I am very stupid oops, this allows jumping between paths


inStr = "xyzabcdefghijklmnopqrstuvw"
alphabet = [chr(i) for i in range(97, 123)]

# Create 
class Node:
    def __init__(self, char, state):
        self.char = char
        self.nextChar = chr(ord(self.char) + 1)
        self.state = state

    
    def buildPaths(self):
        self.paths = []

        # Find all possible paths to next character
        # Base case is z
        if self.char == 'z':
            return
        
        # Base path, cost of 1 to get to next character, state unchanged
        self.paths.append((1, Node(self.nextChar, self.state)))

        # Add in paths to other valid states
        lookStr = self.state
        while True:

            foundPos = lookStr.find(self.nextChar)
            if foundPos <= 0:
                break
            else:
                print(f"Found path to {self.nextChar} from {self.char} at pos {foundPos} in {lookStr}")
                lookStr = lookStr[foundPos+1:]
                self.paths.append((0, Node(self.nextChar, lookStr)))


startNode = Node('a', inStr)
startNode.buildPaths()
print(startNode.paths)