def main():
    n1 = int(input())
    n2 = int(input())
    d = n2 - n1
    if d > 180:
        print(d - 360)
    elif d <= -180:
        print(d + 360)
    else:
        print(d)

if __name__ == "__main__":
    main()
