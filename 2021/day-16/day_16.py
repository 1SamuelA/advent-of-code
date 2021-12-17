import itertools 
import os
from math import prod
from colorama import Fore, Back, Style
import json

RESET = Style.RESET_ALL
DEBUG = True
LiteralValueLeters = ['AAAAA', 'BBBBB', 'CCCCC', 'DDDDD'] 
Packets = []


def debug(msg):
    if DEBUG:
        print(msg)

def Parse(path):
    with open(path) as f:
        hexStr = f.readline()
        hexStr = '38006F45291200'#'EE00D40C823060'#D2FE28'
        #binary = bin(int(hexStr,16))[2:]
        binary = bin(int(hexStr,16))[2:]
        return str(binary)

def GetLiteralValue(binaryStr):
    i = 0
    values = []
    actualString = None
    remainderString = None
    for index, bit in enumerate(binaryStr[::5]):
        i = index * 5 
        # HeaderStr += LiteralValueLeters[i%len(LiteralValueLeters)]
        if int(bit) == 0:
            values.append(binaryStr[i+1:i+5])
            actualString =  binaryStr[:i+5+1]
            remainderString= binaryStr[i+5:] 

            break
        if int(bit) == 1:
            values.append(binaryStr[i+1:i+5])
        i+=1
    
    value = ''.join(values)
    value = int(value,2)

    return actualString, value, remainderString #, HeaderStr

def CreateValuePacket(version, mtype, contents_string, contents_value, binary_length):
    return {
        'version':version,
        'type': mtype,
        'binary_length':binary_length,
        'contents_string':contents_string,
        'value':contents_value
    }

def CreateOpporatorPacket(version, mtype, contents_string, children, binary_length):
    return {
        'version':version,
        'type': mtype,
        'binary_length':binary_length,
        'contents_string':contents_string,
        'children':children
    }

def ReadHeader(binaryStr):
    #Get the Header 
    Header = binaryStr[:6]
    Version = int(Header[:3],2)
    Type = int(Header[3:6],2)

    return Header, Version, Type

def CreatePacket(binaryString):
    print()
    print(binaryString)
                                ##### Get the Header
    HeaderString, Version, Type = ReadHeader(binaryString)
    Remaining = binaryString[6:]
    packetLength = 6
    print("Version: {0}, Type: {1}".format(Version, Type))

    if Type == 4:               ##### Literal Value
        contents, contents_value, remainder = GetLiteralValue(Remaining)
        packetLength += len(contents)
        return remainder, CreateValuePacket(Version,Type,contents,contents_value,packetLength)

    else:                       ##### Operator
        #Get length ID:
        lengthBit = int(Remaining[:1])
        contents = Remaining[1:]
        packetLength += 1
        
        if lengthBit == 1:      ##### then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
            length = 11
            packetLength += length
            subPacketNumber = int(contents[:length],2)
            a = contents[length:]
            packets = []

            for i in range(subPacketNumber):
                a, packet = CreatePacket(a)
                
                packets.append(packet)
            
            packetLength += sum([p['binary_length'] for p in packets])

            return a, CreateOpporatorPacket(Version, Type, contents, packets, packetLength)


        else:                   ##### then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
            length = 15
            packetLength += length
            subPacketLength = int(Remaining[:length],2)
            a = contents[length:]
            packets = []

            i = 0
            while i < subPacketLength:
                a, packet = CreatePacket(a)
                packets.append(packet)
                i+=packet['binary_length']

            packetLength += sum([p['binary_length'] for p in packets])

            return a, CreateOpporatorPacket(Version, Type, contents, packets, packetLength)

                

    



def Solve1(binaryString):
    binaryStr = binaryString
    
    
    packet = CreatePacket(binaryString)
    
    print(json.dumps(packet, indent=2, default=str))
    
    print(Fore.RED + Back.GREEN + "Hello World" + Style.RESET_ALL)
    
    pass

def Solve2(binaryStr):
    pass

if __name__ =="__main__":
    filePath = './example1.txt'
    binaryStr = Parse(filePath)
    print (Solve1(binaryStr))

