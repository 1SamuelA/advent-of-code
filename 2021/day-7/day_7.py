import itertools 
import os


def Parse(path):
    cwd = os.getcwd()
    print(cwd)
    print(cwd+path)
    f = open(path, "r")
    numbers = [int (x) for x in f.readline().split(',')]
    f.close()
    return numbers

def Parse2(crab_positions):
    pass

def Solve1(crab_positions):

    fuel_min = 1000000
    for i in range(max(crab_positions)):
        fuel = 0
        for crab in crab_positions:
            fuel += abs( crab - i)

        if fuel < fuel_min:
            fuel_min = fuel

    return fuel_min


def Solve2(crab_positions):
    fuel_min = 100000000000000000000000000000
    position = 0
    for i in range(max(crab_positions)):
        fuel = 0
        for crab in crab_positions:
            distance = abs( crab - i)
            # 1 + 2 + 3 = 6
            # n(n + 1)/2
            fuel += distance*(distance + 1)//2

        if fuel < fuel_min:
            fuel_min = fuel
            position = i

    return fuel_min

if __name__ =="__main__":
    filePath = "./problem1.txt"
    numbers = Parse(filePath)
    print (Solve1(numbers))
    print (Solve2(numbers))

