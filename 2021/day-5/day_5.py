import itertools 
import os

def Parse(path):
    cwd = os.getcwd()
    boards = []
    with open(path, "r") as f:
        lines = [line for line in f.readlines()] 

        lines =  [line.strip().split(' -> ') for line in lines] 
        lines =  [[[int(cord) for cord in cords.split(',')]  for cords in line] for line in lines] 

    return lines
    

def Solve1(lines):

    

    
    straightLines = []
    Size = [0,0]
    for line in lines:
        #is straight
        start,end = line
        Size[0] = start[0] if start[0] > Size[0] else Size[0]
        Size[0] = end[0] if end[0] > Size[0] else Size[0]
        Size[1] = start[1] if start[1] > Size[1] else Size[1]
        Size[1] = end[1] if end[1] > Size[1] else Size[1]

        if (start[0] == end[0]) | (start[1] == end[1]):
            straightLines.append(line)

    grid = [None] * (Size[0] + 1)
    for index, row in enumerate(grid):
        grid[index] = [0] * (Size[1] + 1)

    

    for line in straightLines:
        start,end = line
        xpoints = []
        ypoints = []
        if start[0] == end[0]:
            xpoints = [start[0]] * abs(start[1] - end[1])
            ypoints = list(range(start[1], end[1]+1 ))
        if start[1] == end[1]:
            xpoints = [start[1]] * abs(start[0] - end[0])
            ypoints = list(range(start[0], end[0]+1))

        print(xpoints)
        print(ypoints)

        lineCords = list(zip(xpoints,ypoints))
        for cord in lineCords:
            grid[cord[0]][cord[1]] += 1
        
    print (grid)
    pass

def Solve2(numbers, boards):
    pass

def CalculateLifeSurport(generatorList, scrubberList, readPos):
    pass

if __name__ =="__main__":
    filePath = './example1.txt'
    lines = Parse(filePath)
    Solve1(lines)


    
    

