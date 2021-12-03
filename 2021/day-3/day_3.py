import itertools 
import os

def Parse(path):
    cwd = os.getcwd()
    print(cwd)
    print(cwd+path)
    f = open(path, "r")
    binaryStringLines = [line.rstrip('\n') for line in f]
    f.close()
    return binaryStringLines

def Parse2(path):
    pass


def Solve1(binaryStringLines):

    width = len(binaryStringLines[0])
    gamma = [''] * width
    epsilon = [''] * width
    height = len(binaryStringLines)

    lists = [0] * width

    for byte in binaryStringLines:
        for index, bit in enumerate(byte):
            lists[index] += int(bit)

    for index, val in enumerate(lists):
        if val > height - val:
            gamma[index] = '1'
            epsilon[index] = '0'
        else :
            gamma[index] = '0'
            epsilon[index] = '1'
    
    gamma = int(''.join(gamma),2)
    epsilon = int(''.join(epsilon),2)

    print(gamma)
    print(epsilon)

    return gamma * epsilon

def Solve2(binaryStringLines):
    
    generatorList, scrubberList = CalculateLifeSurport(binaryStringLines, binaryStringLines, 0)

    
    oxygen_generator_rating = int(''.join(generatorList),2)
    CO2_scrubber_rating = int(''.join(scrubberList),2)

    print(oxygen_generator_rating, CO2_scrubber_rating)

    return oxygen_generator_rating * CO2_scrubber_rating

def CalculateLifeSurport(generatorList, scrubberList, readPos):

    height = len(generatorList)
    if height > 1:
        count = 0
        bit_criteria = 0
        for byte in generatorList:
            count += int(byte[readPos])
            
        if (count >= height - count)  : 
            bit_criteria = '1'
        else: 
            bit_criteria = '0'
        generatorList = list(filter(lambda byte: bit_criteria in byte[readPos], generatorList))



    height2 = len(scrubberList)
    if height2 > 1:
        count2 = 0
        bit_criteria2 = 0
        for byte in scrubberList:
            count2 += int(byte[readPos])

        if count2 < height2 - count2: 
            bit_criteria2 = '1'
        else: 
            bit_criteria2 = '0'

        scrubberList = list(filter(lambda byte: bit_criteria2 in byte[readPos], scrubberList))

    if len(generatorList) > 1 or len(scrubberList) > 1:
        generatorList, scrubberList = CalculateLifeSurport(generatorList, scrubberList, readPos + 1)
        
    
    return generatorList, scrubberList


if __name__ =="__main__":
    filePath = './problem1.txt'
    binaryStringLines = Parse(filePath)
    print (Solve1(binaryStringLines))
    filePath = "./problem1.txt"
    binaryStringLines = Parse(filePath)
    print (Solve2(binaryStringLines))

