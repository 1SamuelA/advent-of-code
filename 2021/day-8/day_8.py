import itertools 
import os

#   0:      1:      2:      3:      4:
#  aaaa            aaaa    aaaa        
# b    c       c       c       c  b    c
# b    c       c       c       c  b    c
#                  dddd    dddd    dddd
# e    f       f  e            f       f
# e    f       f  e            f       f
#  gggg            gggg    gggg        
# 
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

#     Chars   | len |  Fits
# 0 = abc efg |  6  |  null
# 1 =   c  f  |  2  |  0 3 4 7 9
# 2 = a cde g |  5  |  null
# 3 = a cd fg |  5  |  9
# 4 =  bcd f  |  4  |  9
# 5 = ab d fg |  5  |  6 9
# 6 = ab defg |  6  |  null
# 7 = a c  f  |  3  |  0 3 9
# 8 = abcdefg |  7  |  null
# 9 = abcd fg |  6  |  null

# Order = 1 4 7 8 | 0 2 3 5 6 9
# Order = 6 | 0 2 3 5 9
# Order = 9 0 | 2 3 5
# 2 + 4 = 8
# 




# 1 = (c == cf) (f == cf)
# 

# 2 is the only one not to use f
# 9,6,2  

def Parse(path):
    cwd = os.getcwd()
    print(cwd)
    print(cwd+path)
    f = open(path, "r")
    signalsValuePair = f.readlines()
    f.close()
    return signalsValuePair

def Parse2(path):
    pass


def Solve1(signalsValuePair):
    
    pass

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf

# ab = 1
# eafb = 4
# dab = 7
# acedgfb = 8

# 2 = 5
# 3 = 5
# 5 = 5
# 6 = 6
# 9 = 6
# 0 = 6

#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc

def Solve2(signalsValuePairs):
    rows = signalsValuePairs
    part2 = 0
    for row in rows:
        # represent patterns and displayed digits as lists of sets of characters
        patterns, _, digits = row.partition(' | ')
        
        patterns = {frozenset(pattern.strip()) for pattern in patterns.split()}
        digits = [frozenset(digit.strip()) for digit in digits.split()]

        one, seven, four, eight = known_digits = [get_digits_by_length(patterns, n)[0] for n in [2, 3, 4, 7]]
        
        patterns -= set(known_digits)

        six = next(pattern for pattern in patterns if pattern | one == eight)
        patterns.remove(six)

        # remaining 6-segment digits: "0" and "9", and only "9" contains "4"
        six_segments = get_digits_by_length(patterns, 6)
        for digit in six_segments:
            if four < digit:
                nine = digit
            else:
                zero = digit
        patterns -= {zero, nine}

        two = next(pattern for pattern in patterns if pattern | four == eight)
        three = next(pattern for pattern in patterns if one < pattern)
        patterns -= {two, three}
        five = patterns.pop()

        digit_list = [zero, one, two, three, four, five, six, seven, eight, nine]
        proper_digits = (digit_list.index(digit) for digit in digits)
        a = ''.join(map(str, proper_digits))
        print(a)
        part2 += int(a)

    return part2


def get_digits_by_length(patterns, length):
    """Find all digits of a given length."""
    return [pattern for pattern in patterns if len(pattern) == length]


if __name__ =="__main__":
    filePath = "./example1.txt"
    signalsValuePair = Parse(filePath)
    print (Solve2(signalsValuePair))

