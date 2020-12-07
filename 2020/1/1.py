import argparse


class Programme:
    def __init__(self, args):
        FilePath = args.FilePath

        with open(FilePath, mode='r') as f:
            self.filelines = f.read().splitlines()

        

    def run(self):
        #ParseData
        numbers = []
        for line in self.filelines:
            numbers.append(int(line))

        print(numbers)

        #add togeather to find which numbers add to 2020

        result = 0

        for i in range(len(numbers)):
            first = numbers[i]
            for j in range(len(numbers)):
                if i == j:
                    continue
                second = numbers[j]

                if (first + second) == 2020:
                    result = first * second
                    break

            if result != 0:
                break

        print(result)

    def run2(self):
        #ParseData
        numbers = []
        for line in self.filelines:
            numbers.append(int(line))

        #add togeather to find which numbers add to 2020

        result = 0

        for i in range(len(numbers)):
            first = numbers[i]
            for j in range(len(numbers)):
                if i == j:
                    continue
                second = numbers[j]
                for k in range(len(numbers)):
                    if i == k:
                        continue
                    if j == k:
                        continue
                    third = numbers[k]

                    if (first + second + third) == 2020:
                        result = first * second * third
                        break

                if result != 0:
                    break

            if result != 0:
                break

        print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")

    parser.add_argument('--FilePath',
                        required=True)

    args = parser.parse_args()

    p = Programme(args)
    p.run2()