def main():
    n = int(input())
    weak = []
    for i in range(n):
        line = input()
        if line.count("1") < 3:
            weak.append(str(i))
    print(" ".join(weak))

if __name__ == "__main__":
    main()
