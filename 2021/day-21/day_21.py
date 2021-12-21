import itertools 
import os
from math import prod
from colorama import Fore, Back, Style
import json
import sys

DEBUG = True

class DeterministicDie():
    def __init__(self):
        self.__value = 0
        self.__size = 100

    def roll(self, NumRolls):
        value = 0
        value = ((self.__value + NumRolls)*(self.__value + NumRolls + 1)//2) - (self.__value*(self.__value + 1)//2)
        self.__value += NumRolls
        if self.__value > 100:
            self.__value - 100
        return value



def debug(msg):
    if DEBUG:
        print(msg)

def Parse(path):
    with open(path) as f:
        input = f.readlines()
        
        playerOne = int(input[0].split(':')[1].strip())
        playerTwo = int(input[1].split(':')[1].strip())

        return playerOne, playerTwo


def Solve1(playerOne, playerTwo):


    running = True
    boardPositions = 10
    playerOneScore, playerTwoScore = [0,0]
    die = DeterministicDie()
    rolls = 0
    Turn = 1

    while running:
        movement = die.roll(3)
        #print(movement)
        rolls += 3
        #Player1
        if Turn == 1:
            playerOne += movement
            playerOne = 10 if playerOne%boardPositions == 0 else playerOne%boardPositions
            playerOneScore += playerOne
            Turn = 2
        elif Turn == 2:
            playerTwo += movement
            playerTwo = 10 if playerTwo%boardPositions == 0 else playerTwo%boardPositions
            playerTwoScore += playerTwo
            Turn = 1

        if (playerOneScore >= 1000) or (playerTwoScore >= 1000):
            running = False

    lowest = playerTwoScore if playerTwoScore < playerOneScore else playerOneScore
    # print(Fore.RED + Back.GREEN + str((lowest,rolls) ) + Style.RESET_ALL)
    # print(Fore.RED + Back.GREEN + str(lowest * rolls) + Style.RESET_ALL)

    return lowest * rolls
    
    pass

def Solve2(playerOne, playerTwo):
    # Wow Head Hurts
    pass

if __name__ =="__main__":
    filePath = './problem1.txt'
    playerOne, playerTwo = Parse(filePath)
    print (Solve1(playerOne, playerTwo))

