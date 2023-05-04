# Input: A valid game state for a 2048 puzzle
# First four lines of input describe 16 integers in a 4x4 grid
# Constrained to {0, 2, 4, 8, 16, 32, 64, 128, 245, 512, 1024}
# Fifth line of input denotes integer describing movement:
# 0 - left
# 1 - up
# 2 - right
# 3 - down

# Output: New game state after executing movement


gameState = []

for i in range(4):
    row = input().split()
    gameState.append(row)

move = int(input())



# Create function to repurpose left and right for verticality
def transpose(board):
    newBoard = []

    for i in range(4):
        newCol = []
        for j in range(4):
            newCol.append(board[j][i])
        newBoard.append(newCol)

    return newBoard

# Verify Transpose works

# print("Original")
# for i in range(4):
#     print(gameState[i])

# print("Transpose")
# transposedGame = transpose(gameState)
# for i in range(4):
#     print(transposedGame[i])

def performMove(board, move):
    if move == 1 or move == 3:
        state = transpose(board)
    else:
        state = board
    
    if move == 2 or move == 3:
        for i in range(4):
            state[i].reverse()
    
    
    for i in range(4):
        # Remove all 0s, effectively moving everything to one side
        state[i] = [j for j in state[i] if j != "0"]
        # Merge adjacent values in pairs
        lastVal = -1
        lastValPos = -1
        prunedPos = []
        for num, j in enumerate(state[i]):
            if j == lastVal:
                # Increase value
                state[i][num] = str(int(j) * 2)
                # Mark pruned value for removal
                prunedPos.append(lastValPos)
                lastVal = -1
                lastValPos = -1
            else:
                lastVal = j
                lastValPos = num
        
        # Remove Pruned in reverse order
        prunedPos.reverse()
        for val in prunedPos:
            state[i].pop(val)
            pass
        
        # Add 0s on the end to represent new empty space
        spaces = 4 - len(state[i])
        for newSpace in range(spaces):
            state[i].append("0")

    
    
    # Put board back in proper order
    if move == 2 or move == 3:
        for i in range(4):
            state[i].reverse()
    
    if move == 1 or move == 3:
        state = transpose(state)
    else:
        state = state

    return state

endState = performMove(gameState, move)

for i in endState:
    print(" ".join(i))