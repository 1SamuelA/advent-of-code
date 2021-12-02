FORWARD = 'forward' 
DOWN = 'down' 
UP = 'up' 



def Parse(path):
    f = open(path, "r")
    instructions = [line.rstrip('\n') for line in f]
    f.close()
    return instructions

def Parse2(path):
    pass


def Solve1(instructions):
    positionx = 0
    positiony = 0

    for instruction in instructions:
        direction, distance = instruction.split(' ')
        distance = int(distance)
        if direction == FORWARD:
            positionx += distance
        if direction == DOWN:
            positiony += distance
        if direction == UP:
            positiony -= distance

    return positionx * positiony 
        

def Solve2(lines):
    positionx = 0
    positiony = 0
    aim = 0

    for instruction in instructions:
        direction, distance = instruction.split(' ')
        distance = int(distance)
        if direction == FORWARD:
            positionx += distance
            positiony += aim*distance
        if direction == DOWN:
            aim += distance
        if direction == UP:
            aim -= distance

    return positionx * positiony 


if __name__ =="__main__":
    filePath = "./problem1.txt"
    instructions = Parse(filePath)
    print (Solve2(instructions))

