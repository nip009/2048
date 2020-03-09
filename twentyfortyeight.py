# Link to the problem: https://open.kattis.com/problems/2048


def printArr(grid):
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[i])):
            if(j != 3):
                row += str(grid[i][j]) + " "
            else:
                row += str(grid[i][j])
        print(row)


def transpose(l1):
    '''
    Takes a 2d list (a list of lists) and returns the transpose of that 2d list.
    '''
    l2 = []
    for i in range(len(l1[0])):
        row = []
        for item in l1:
            row.append(item[i])
        l2.append(row)
    return l2


def sortZeroesToRightAndMerge(grid):
    '''
    Sort values so that zero is on the right side and values are merged once.
    '''
    for i in range(len(grid)):
        for j, _ in reversed(list(enumerate(grid[i]))):
            # Move numbers not equal to zero over to the right side.
            grid[i].sort(key=lambda x: x != 0)
            if(grid[i][j] == 0):
                continue
            if(j > 0 and grid[i][j-1] == grid[i][j]):
                grid[i][j-1] *= 2
                grid[i][j] = 0
    return grid


def sortZeroesToLeftAndMerge(grid):
    '''
    Sort values so that zero comes to the left and values are merged once.
    '''
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i].sort(key=lambda x: x != 0, reverse=True)
            if(grid[i][j] == 0):
                continue
            if(j > 0 and grid[i][j-1] == grid[i][j]):  # 2 2 0 0 -> 4 0 0 0
                grid[i][j-1] *= 2
                grid[i][j] = 0
    return grid


def goLeft(grid):
    grid = sortZeroesToLeftAndMerge(grid)
    return grid


def goRight(grid):
    grid = sortZeroesToRightAndMerge(grid)
    return grid


def goUp(grid):
    grid = transpose(grid)
    grid = sortZeroesToLeftAndMerge(grid)
    grid = transpose(grid)
    return grid


def goDown(grid):
    grid = transpose(grid)
    grid = sortZeroesToRightAndMerge(grid)
    grid = transpose(grid)
    return grid

def runGame(move):
    global grid
    if move == 0:  # left
        return goLeft(grid)
    elif move == 1:  # up
        return goUp(grid)
    elif move == 2:  # right
        return goRight(grid)
    elif(move == 3):  # down
        return goDown(grid)



grid = [[0 for i in range(4)] for j in range(4)]
for i in range(4):
    inp = input().split(" ")
    for j in range(4):
        grid[i][j] = int(inp[j])
move = int(input())
grid = runGame(move)
printArr(grid)


