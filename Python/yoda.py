def main():
    n1 = input()
    n2 = input()
    new1 = ""
    new2 = ""
    shorter = min(len(n1), len(n2))
    longer = max(len(n1), len(n2))
    n1 = n1.zfill(longer)
    n2 = n2.zfill(longer)
    for i in range(longer):
        if n1[i] > n2[i]:
            new1 += n1[i]
        elif n1[i] < n2[i]:
            new2 += n2[i]
        else:
            new1 += n1[i]
            new2 += n2[i]
    
    if len(new1) == 0:
        print("YODA")
    else:
        print(int(new1))
    if len(new2) == 0:
        print("YODA")
    else:
        print(int(new2))

    
if __name__ == "__main__":
    main()
