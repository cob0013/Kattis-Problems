days = [31, , 31, 30, 31, 30, 31, 31, 30, 31, 30. 31]
def main():
    year = [0 for i in range(365)]
    n = int(input())
    for i in range(n):
        name, date = input().split()
        m, d = map(int, date.split("-"))
        year[(days[m - 1]

if __name__ == "__main__":
    main()




