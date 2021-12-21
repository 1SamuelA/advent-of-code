import itertools 
import os
from math import prod
from colorama import Fore, Back, Style
import json
import sys

DEBUG = True



def debug(msg):
    if DEBUG:
        print(msg)

def print2dArray(rows):
    lines = []
    for row in rows:
        line = ''.join([str(a) for a in row])
        lines.append(str(line))

    print('\n'.join(lines))
    
def Parse(path):
    with open(path) as f:
        lines = f.readlines()

        rows = [None] * len(lines)

        for index, line in enumerate(lines):
            rows[index] = [int(element) for element in line.strip()]
        print2dArray(rows)

        return rows

def AStar(rows, node):
    pass

def Solve1(rows):
    height = len(rows)
    width = len(rows[0])

    start = (0,0)
    end = (width - 1, height - 1)

    startNode = rows[0][0]
    endNode = rows[-1][-1]

    print(start, startNode, end, endNode)

    




    print(Fore.RED + Back.GREEN + "Hello World" + Style.RESET_ALL)
    
    pass

def Solve2(binaryStr):
    pass

if __name__ =="__main__":
    filePath = './example1.txt'
    rows = Parse(filePath)
    print (Solve1(rows))

