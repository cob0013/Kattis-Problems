import math
def main():
    b, k, g = map(float, input().split())
    groups = k // g 
    print(math.ceil((b - 1) / groups))

if __name__ == "__main__":
    main()
