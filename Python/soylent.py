import math
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(math.ceil(n / 400))
if __name__ == "__main__":
    main()
