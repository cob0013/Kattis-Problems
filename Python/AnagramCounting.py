import math


def main():
    while True:
        try:
            word = input()
            count = dict()
            for letter in word:
                if letter in count:
                    count[letter] += 1
                else:
                    count[letter] = 1
            output = math.factorial(len(word))
            for frequency in count.values():
                output //= math.factorial(frequency)

            print(output)

        except:
            break

if __name__ == "__main__":
    main()
