import itertools 
import os


def Parse(path):
    cwd = os.getcwd()
    print(cwd)
    print(cwd+path)
    f = open(path, "r")
    initalState = [int (x) for x in f.readline().split(',')]
    f.close()
    return initalState

def Parse2(initalState):
    pass

def Solve1(initalState):

    state = [0] * 9

    state[1] = len(list(filter(lambda num: num == 1, initalState)))
    state[2] = len(list(filter(lambda num: num == 2, initalState)))
    state[3] = len(list(filter(lambda num: num == 3, initalState)))
    state[4] = len(list(filter(lambda num: num == 4, initalState)))
    state[5] = len(list(filter(lambda num: num == 5, initalState)))

    numDays = 80
    for day in range(numDays):
        newState = [0] * 9
        newState[0] = state[1]
        newState[1] = state[2]
        newState[2] = state[3]
        newState[3] = state[4]
        newState[4] = state[5]
        newState[5] = state[6]
        newState[6] = state[0] + state[7]
        newState[7] = state[8]
        newState[8] = state[0]

        state = newState

    return sum(state)
        
def Solve2(initalState):
    state = [0] * 9

    state[1] = len(list(filter(lambda num: num == 1, initalState)))
    state[2] = len(list(filter(lambda num: num == 2, initalState)))
    state[3] = len(list(filter(lambda num: num == 3, initalState)))
    state[4] = len(list(filter(lambda num: num == 4, initalState)))
    state[5] = len(list(filter(lambda num: num == 5, initalState)))

    numDays = 256
    for day in range(numDays):
        newState = [0] * 9
        newState[0] = state[1]
        newState[1] = state[2]
        newState[2] = state[3]
        newState[3] = state[4]
        newState[4] = state[5]
        newState[5] = state[6]
        newState[6] = state[0] + state[7]
        newState[7] = state[8]
        newState[8] = state[0]

        state = newState

    return sum(state)

if __name__ =="__main__":
    filePath = "./problem1.txt"
    numbers = Parse(filePath)
    #print (Solve1(numbers))
    print (Solve2(numbers))