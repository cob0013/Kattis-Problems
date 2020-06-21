
def main():
    n1 = input()
    n2 = input()
    if len(n1) < len(n2):
        n1 = n1.zfill(len(n2))
    move = len(n1) -  len(n2) + 1
    print((n1[:move] + "." +  n1[move:].rstrip("0")).rstrip("."))
    
if __name__ == "__main__":
    main()
