import io, os, time

# Fast I/O
# input = io.BytesIO(os.read(0, \
#          os.fstat(0).st_size)).readline

numCouples, numInstructions = input().split()

congaHead = None
congaTail = None

class Person:
    def __init__(self, name, partnerName):
        self.name = name
        self.partnerName = partnerName
        self.partner = None
        self.Forward = None
        self.Backward = None

class LineInfo:
    def __init__(self, congaHead, congaTail, micDude):
        self.congaHead = congaHead
        self.congaTail = congaTail
        self.micDude = micDude


p1, p2 = input().split()
congaHead = Person(p1, p2)
micDude = congaHead
congaTail = Person(p2, p1)
congaHead.partner = congaTail
congaTail.partner = congaHead
congaHead.Backward = congaTail
congaTail.Forward = congaHead
micDude = congaHead

line = LineInfo(congaHead, congaTail, micDude)

for couple in range(int(numCouples) - 1):
    p1, p2 = input().split()
    Person1 = Person(p1, p2)
    Person2 = Person(p2, p1)
    Person1.partner = Person2
    Person2.partner = Person1
    line.congaTail.Backward = Person1
    Person1.Forward = line.congaTail
    line.congaTail = Person1
    line.congaTail.Backward = Person2
    Person2.Forward = line.congaTail
    line.congaTail = Person2
    

instructions = input()

def F(line):
    line.micDude = line.micDude.Forward

def B(line):
    line.micDude = line.micDude.Backward

def R(line):
    # Pass Mic
    movedDude = line.micDude
    if (line.micDude.Backward == None):
        line.micDude = line.congaHead
    else:
        line.micDude = line.micDude.Backward
    
    # Move to back of line
    if (movedDude == line.congaHead):
        # Reassign conga head if necessary
        line.congaHead = movedDude.Backward
    # Reassign neighbors
    if (movedDude.Backward != None):
        movedDude.Backward.Forward = movedDude.Forward
    if (movedDude.Forward != None):
        movedDude.Forward.Backward = movedDude.Backward
    
    line.congaTail.Backward = movedDude
    movedDude.Forward = line.congaTail
    movedDude.Backward = None
    line.congaTail = movedDude

def C(line):
    # Pass Mic
    movedDude = line.micDude
    if (line.micDude.Backward == None):
        line.micDude = line.congaHead
    else:
        line.micDude = line.micDude.Backward

    # Reassign conga head/tail if necessary
    if movedDude == line.congaHead:
        line.congaHead = movedDude.Backward

    if movedDude == line.congaTail:
        line.congaTail = movedDude.Forward
    
    # Reassign neighbors
    if (movedDude.Backward != None):
        movedDude.Backward.Forward = movedDude.Forward
    if (movedDude.Forward != None):
        movedDude.Forward.Backward = movedDude.Backward

    movedDude.Forward = movedDude.partner
    movedDude.Backward = movedDude.partner.Backward
    movedDude.partner.Forward = movedDude.partner.Backward
    movedDude.partner.Backward = movedDude

    if movedDude.Backward != None:
        movedDude.Backward.Forward = movedDude
    if movedDude.partner.Forward != None:
        movedDude.partner.Forward.Backward = movedDude.partner
    
    

def P(line):
    print(line.micDude.partnerName)

instructionActions = {
    'F' : F,
    'B' : B,
    'R' : R,
    'C' : C,
    'P' : P
}

for letter in instructions:
    instructionActions[letter](line)

print()

lineInOrder = []

personIter = line.congaTail
while personIter != None:
    lineInOrder.append(personIter.name)
    personIter = personIter.Forward

lineInOrder.reverse()
for pers in lineInOrder:
    print(pers)