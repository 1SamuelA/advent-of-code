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

def Parse(path):
    with open(path) as f:
        program, image = f.read().split("\n\n",1)
        print(program)
        print()
        print(image)

        program = EnhancementProgram(program)

        return program, image

class EnhancementProgram:
    def __init__(self, program):
        self._program = program

    def getCode(self, index):
        if index < 512:
            return self._program[index]
        else:
            raise SystemExit('Program Cant Access')

class Grid:
    def __init__(self):
        self.repository={}

    def CreateRepos(self, a):
        pass

def Solve1(binaryString):

    print(Fore.RED + Back.GREEN + "Hello World" + Style.RESET_ALL)
    
    pass

def Solve2(binaryStr):
    pass

if __name__ =="__main__":
    filePath = './example1.txt'
    binaryStr = Parse(filePath)
    #print (Solve1(binaryStr))

