import argparse


class Programme:
    def __init__(self, args):
        FilePath = args.FilePath

        with open(FilePath, mode='r') as f:
            self.filelines = f.read().splitlines()

    def run(self):
        #ParseData
        rows = []
        for line in self.filelines:
            row = []
            for place in line:
                if place == '.':
                    row.append(0)
                elif place == '#':
                    row.append(1)
            rows.append(row)
        # Proccess
        maxHeight = len(rows)
        MaxWidth = len(rows[0])
        positionX = 0
        positionY = 0
        travel = [3,1]

        treeCount = 0

        while positionY < maxHeight:
            #Check Position
            treeCount = treeCount + rows[positionY][positionX]
            positionX =(positionX + travel[0]) % MaxWidth
            positionY =positionY + travel[1]
            
        print(treeCount)

    def run2(self):
        #ParseData
        rows = []
        for line in self.filelines:
            row = []
            for place in line:
                if place == '.':
                    row.append(0)
                elif place == '#':
                    row.append(1)
            rows.append(row)
        total = 1
        total = self.Test(rows, [1,1])
        total = total * self.Test(rows, [3,1])
        total = total * self.Test(rows, [5,1])
        total = total * self.Test(rows, [7,1])
        total = total * self.Test(rows, [1,2])

        print(total)
    
    def Test(self, rows, travel):
        maxHeight = len(rows)
        MaxWidth = len(rows[0])
        positionX = 0
        positionY = 0
        treeCount = 0

        while positionY < maxHeight:
            #Check Position
            treeCount = treeCount + rows[positionY][positionX]
            positionX =(positionX + travel[0]) % MaxWidth
            positionY =positionY + travel[1]

        return treeCount

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")

    parser.add_argument('--FilePath',
                        required=True)

    args = parser.parse_args()

    p = Programme(args)
    p.run2()