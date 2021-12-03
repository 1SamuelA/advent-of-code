import argparse
import json

class Programme:
    def __init__(self, args):
        FilePath = args.FilePath

        with open(FilePath, mode='r') as f:
            self.filelines = f.read().splitlines()

    def run1(self):
        #ParseData
        rows = []
        passports = []

        for line in self.filelines:
            if line == '':
                passport = self.makePassport(rows)
                passports.append(passport)
                rows = []
                continue
            rows.append(line)

        print(passports[0])
        print(json.dumps(json.loads(passports[0]),indent=4))

    def makePassport(self, data):
        mString = ' '.join(data)
        array = mString.split(' ')
        newArray = []
        for element in array:
            string = "\"{0}\"".format(element.split(':')[0])+':'+"\"{0}\"".format(element.split(':')[1])
            print (string)
            newArray.append(string)
        
        return "{ \"data\": " + "{ {0} }".format(' , '.join(newArray)) + "}"
    
    def run2(self):
        pass
    
    def Test(self, rows, travel):
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")

    parser.add_argument('--FilePath',
                        required=True)

    args = parser.parse_args()

    p = Programme(args)
    p.run1()