def main():
    previous = input()
    startswith = dict()
    lastLetter = previous[-1]
    n = int(input())
    avaliable = []
    for i in range(n):
            animal = input()
            avaliable.append(animal)
            if animal[0] not in startswith:
                    startswith[animal[0]] = []
            startswith[animal[0]].append(animal)
    foundFirst = False
    first = ""
    if lastLetter not in startswith:
            print("?")
            return
    for animal in avaliable:
            if animal[0] == lastLetter:
              lookingfor = animal[-1]
              if lookingfor not in startswith or (len(startswith[lookingfor]) == 1 and startswith[lookingfor][0] == animal):
                    print(animal + "!")
                    return
              if not foundFirst:
                    foundFirst = True
                    first = animal

    print(first)


if __name__ == "__main__":
        main()
