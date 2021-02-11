def main():
    dwarves = []
    for i in range(9):
        dwarves.append(int(input()))
    for i in range(9):
        for j in range(i + 1, 9):
            seven_dwarves = [] 
            for k in range(9):
                if k != i and k != j:
                    seven_dwarves.append(dwarves[k])
            if sum(seven_dwarves) == 100:
                for dwarf in seven_dwarves:
                    print(dwarf)
                return


if __name__ == "__main__":
    main()
