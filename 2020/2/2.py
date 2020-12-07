import argparse


class Programme:
    def __init__(self, args):
        FilePath = args.FilePath

        with open(FilePath, mode='r') as f:
            self.filelines = f.read().splitlines()

        

    def run(self):
        #ParseData
        Sets = []
        for line in self.filelines:
            # Split scheme and password
            scheme = line.split(':',1)[0]
            password = line.split(':',1)[1]

            # Split the scheme
            minRange = int(scheme.split('-',1)[0])
            maxRange = int(scheme.split('-',1)[1].split(' ',1)[0])
            char = scheme.split('-',1)[1].split(' ',1)[1]
            print (minRange)
            print (maxRange)
            print (char)

            Sets.append([minRange, maxRange, char, password])

        # Proccess

        failed = passed = 0

        for test in Sets:
            letterCount = test[3].count(test[2])
            if test[0] <= letterCount <= test[1]:
                passed = passed + 1
            else:
                failed = failed + 1

        print('Passed: ')
        print(passed )
        print('Failed: ')
        print(failed )

    def run2(self):
        #ParseData
        Sets = []
        for line in self.filelines:
            # Split scheme and password
            scheme = line.split(':',1)[0]
            password = line.split(':',1)[1]

            # Split the scheme
            minRange = int(scheme.split('-',1)[0])
            maxRange = int(scheme.split('-',1)[1].split(' ',1)[0])
            char = scheme.split('-',1)[1].split(' ',1)[1]
            print (minRange)
            print (maxRange)
            print (char)

            Sets.append([minRange, maxRange, char, password])

        # Proccess

        failed = passed = 0

        for test in Sets:
            pos1 = test[0]
            pos2 = test[1]
            character = test[2]
            password = test[3]
            
            result = False
            
            if password[pos1] == character:
                if password[pos2] != character:
                    result = True

            if password[pos2] == character:
                if password[pos1] != character:
                    result = True

            if result:
                passed = passed + 1
            else:
                failed = failed + 1

        print('Passed: ')
        print(passed )
        print('Failed: ')
        print(failed )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")

    parser.add_argument('--FilePath',
                        required=True)

    args = parser.parse_args()

    p = Programme(args)
    p.run2()