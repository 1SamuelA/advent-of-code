import itertools 
import os
from math import prod

def Parse(path):
    with open(path) as f:
        rows = f.read().splitlines()
        rows = [[int(value) for value in row] for row in rows]
        height = len(rows)
        width = len(rows[0])

        count = 0
        lowPoints = []

        for y,row in enumerate(rows):
            for x,value in enumerate(row):
                a = set()
                if y > 0:
                    a.add(value < rows[y - 1][x])
                if y < height - 1:
                    a.add(value < rows[y + 1][x])
                if x > 0:
                    a.add(value < rows[y][x - 1])
                if x < width - 1:
                    a.add(value < rows[y][x + 1])

                happen = True
                for b in a:
                    if b == False:
                        happen = False
                
                if happen:
                    lowPoints.append([x,y])
                    count += int(value) + 1 

        print(lowPoints)
        counts = []
        for lowPoint in lowPoints:
            print("NEW POINT")
            startX, startY = lowPoint
            counts.append(Search(lowPoint,rows))
        
        
        print(prod(sorted(counts, reverse=True)[:3]))

    pass

def Search(point, rows):
    print(point)
    y, x = point
    count = 0

    if rows[x][y] == 9:
        return 0
        
    else:
        try:
            rows[x][y] = 9
        except:
            exit(1)
        
        count += 1
        #Up
        if y > 0:
            count += Search([y-1,x], rows)
        #Right
        if x < len(rows)-1:
            count += Search([y,x+1], rows)
        #Down
        if y < len(rows[0])-1:
            count += Search([y+1,x], rows)
        #Right
        if x > 0:
            count += Search([y,x-1], rows) 
        #Right
    return count
    

def Parse2(path):
    pass

def Solve1(binaryStringLines):
    pass

def Solve2(binaryStringLines):
    pass

if __name__ =="__main__":
    filePath = './problem1.txt'
    grid = Parse(filePath)
    print (Solve1(grid))

