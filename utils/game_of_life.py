from random import choice
import copy, random, sys, time

def CreateStart(x,y):
    grid=[None]*x
    
    for i in range(0,x):
        grid[i] = [None]*y 
        for j in range(0,y):
            grid[i][j] = choice([0, 1])


    return grid

def DisplayGrid(grid):
    print('\n' * 50)
    for row in grid:
        string = ''
        for element  in row:
            if element == 1:
                string += '#'
            else:
                string += ' '
            string += ' '
        print(string)

def Update(state):
    oldState=state
    newState=state

    # Go though grid and check neighbours
    # Remeber to watch for edge cases
    width = len(state)
    height = len(state[0])

    for i in range(0,height):
        for j in range(0, height):
            numberOfAliveNeighbours = 0
            if i > 0:
                numberOfAliveNeighbours += oldState[i-1][j]
            if i < width-1:  
                numberOfAliveNeighbours += oldState[i+1][j]
            if j > 0:
                numberOfAliveNeighbours += oldState[i][j-1]
            if j < height-1:  
                numberOfAliveNeighbours += oldState[i][j+1]
            if i > 0 and j > 0:
                numberOfAliveNeighbours += oldState[i-1][j-1]
            if i < width-1 and j < height-1:
                numberOfAliveNeighbours += oldState[i+1][j+1]
            if (i > 0) and (j < height-1):
                numberOfAliveNeighbours += oldState[i-1][j+1]
            if i < width-1 and j > 0:
                numberOfAliveNeighbours += oldState[i+1][j-1]



            if oldState[i][j]==1:
                if numberOfAliveNeighbours == 3 or numberOfAliveNeighbours == 2:
                    newState[i][j] = 1
                else:
                    newState[i][j] = 0
            elif oldState[i][j]==0:
                if numberOfAliveNeighbours == 3:
                    newState[i][j] = 1
                else:
                    newState[i][j] = 0

    return newState


if __name__ == "__main__":
    initialState = CreateStart(10,10)
    DisplayGrid (initialState)
    state = initialState
    while True:

        state = Update (initialState)
        DisplayGrid (state)

        try:
            time.sleep(1)  # Add a 1 second pause to reduce flickering.
        except KeyboardInterrupt:
            print("Conway's Game of Life")
            print('By Al Sweigart al@inventwithpython.com')
            sys.exit()  # When Ctrl-C is pressed, end the program.