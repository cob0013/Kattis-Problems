def main():
    n = int(input())
    yours = input()
    friends = input()
    diff = 0
    same = 0
    for i in range(len(yours)):
        if yours[i] == friends[i]:
            same += 1

    print((len(yours) - abs(n -  same)))

if __name__ == "__main__":
    main()
