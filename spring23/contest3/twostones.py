numStones = int(input())

afterNrounds = numStones % 4

if afterNrounds % 2 == 0:
    print("Bob")
else:
    print("Alice")