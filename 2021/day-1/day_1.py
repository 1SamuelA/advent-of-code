
from 


def Parse(path):
    f = open(path, "r")
    depths = [int(line.rstrip('\n')) for line in f]
    f.close()
    return depths

def Parse2(path):
    f = open(path, "r")
    depths = [int(line.rstrip('\n')) for line in f]
    f.close()

    #Creating a list of sums
    # 199  A      
    # 200  A B    
    # 208  A B C  
    # 210    B C D
    # 200  E   C D
    # 207  E F   D
    # 240  E F G  
    # 269    F G H
    # 260      G H
    # 263        H
    sums = []
    for i in range(2, len(depths)):
        sums.append(depths[i] + depths[i-1] + depths[i-2]) 
    
    return sums

def Solve1(lines):
    increased = 0;
    last = -1
    for i in range(1, len(lines)):
        diffrence = lines[i] - lines[i-1]
        if diffrence > 0:
            increased += 1

    return increased

def Solve2(lines):
    increased = 0;
    sums = []
    last = -1
    for i in range(1, len(lines)):
        diffrence = lines[i] - lines[i-1]
        if diffrence > 0:
            increased += 1

    return increased

if __name__ =="__main__":
    filePath = "./problem1.txt"
    depths = Parse(filePath)
    print (Solve1(depths))
    filePath2 = "./problem2.txt"
    depths = Parse2(filePath2)
    print (Solve1(depths))


        
        