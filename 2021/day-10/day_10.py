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

    charSetOpen = {'(':')', '[':']', '{':'}', '<':'>'}
    charSetValue = {')':3, ']':57, '}':1197, '>':25137}
    values = []
    currupted = []
    master = lines
    for line in master:
        valid = False
        openChar = [line[0]]
        for char in line[1:]:

            # [([]))
            # [         - Open - ExpectAnyOpen or ]
            # [(        - Open - ExpectAnyOpen or )
            # [([       - Open - ExpectAnyOpen or ]
            # [([]      - Open - ExpectAnyOpen or )
            # [([])     - Open - ExpectAnyOpen or ]
            # [([]))    - BREAK - ExpectAnyOpen or ]
            
            # Check if open
            if char in ['(', '[', '{', '<']:
                openChar.append(char)
                continue

            # Check if 
            if char == charSetOpen[openChar[-1]]:
                openChar.pop()
                continue
            if char not in charSetOpen:
                values.append(charSetValue[char])
                currupted.append(line)
                break
            
    print(sum(values))
    print()

    for cur in currupted:
        master.remove(cur)

    endings = []
    endingsValue = {')':1, ']':2, '}':3, '>':4}
    for line in master:
        openChar = [line[0]]
        for char in line[1:]:
            
            # Check if open
            if char in ['(', '[', '{', '<']:
                openChar.append(char)
                continue

            # Check if 
            if char == charSetOpen[openChar[-1]]:
                openChar.pop()
                continue
            
        ending = [charSetOpen[a] for a in openChar]
        ending.reverse()
        score = 0
        for value in ending:
            score = score * 5
            score += endingsValue[value]

        print(openChar)
        endings.append(score)
        
    index = (len(endings) - 1)//2
    endings = sorted(endings)

    print()
    print(Fore.RED + Back.GREEN + str(endings[index]) + Style.RESET_ALL)
    
    pass

def Solve2(binaryStringLines):
    pass

if __name__ =="__main__":
    filePath = './problem1.txt'
    rows = Parse(filePath)
    print (Solve1(rows))

