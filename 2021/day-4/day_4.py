import itertools 
import os

class Board:
    def __init__(self, grid):
        rows = grid
        cols = list(zip(*grid))

        self.candidates = [set(candidate) for candidate in rows + cols]
        

        self.all_nums = set()
        for row in grid:
            self.all_nums.update(row)

    def bingo(self, called_out):
        # If a line (row or col) is a subset of the numbers called -> BINGO!
        return any(line <= called_out for line in self.candidates)

    def score(self, called_out):
        return sum(self.all_nums - called_out)

    def __str__(self):
        return "Hey"

    def __repr__(self):
        return self.__str__()

def Parse(path):
    cwd = os.getcwd()
    boards = []
    with open(path, "r") as f:
        numbers = [int(num) for num in f.readline().split(',')] 
        f.readline()

        for board in f.read().split('\n\n'):
            grid = []
            for line in board.splitlines():
                row = list(map(int, line.split()))
                grid.append(row)
            boards.append(Board(grid))
    
    return numbers, boards
    
def Parse2(path):
    pass

def Solve1(numbers, boards):
    called_out = set()
    for num in numbers:
        called_out.add(num)

        for grid in boards:
            if grid.bingo(called_out):
                print(num * grid.score(called_out))
                boards.remove(grid)
                return num * grid.score(called_out)

            

def Solve2(numbers, boards):
    called_out = set()
    for num in numbers:
        called_out.add(num)

        for grid in boards:
            if grid.bingo(called_out):
                boards.remove(grid)

            if len(boards) == 0:
                # We have removed the last grid. so print this one.
                print(num * grid.score(called_out))
                return num * grid.score(called_out)

def CalculateLifeSurport(generatorList, scrubberList, readPos):
    pass

if __name__ =="__main__":
    filePath = './problem1.txt'
    numbers, boards = Parse(filePath)
    Solve1(numbers, boards)
    Solve2(numbers, boards)

    
    

