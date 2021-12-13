import itertools 
import os
from math import prod
from colorama import Fore, Back, Style

def Parse(path):
    with open(path) as f:
        rows = set(f.read().splitlines())
        return rows


def Parse2(path):
    pass

def Solve1(lines):

    
    print(Fore.RED + Back.GREEN + "Hello World" + Style.RESET_ALL)
    
    pass

def Solve2(binaryStringLines):
    pass

if __name__ =="__main__":
    filePath = './problem1.txt'
    rows = Parse(filePath)
    print (Solve1(rows))

