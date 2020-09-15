def main():
    n, q = map(int, input().split())
    wealth = dict()
    curr = 0
    for i in range(q):
        event = input().split()
        cmd = event[0]
        if cmd == "SET":
            wealth[int(event[1])-1] = int(event[2])
        elif cmd == "RESTART":
            curr = int(event[1])
            wealth.clear()
        else:
            
            x = int(event[1]) - 1
            if x not in wealth:
                print(curr)
            else:
                print(wealth[x])
            

if __name__ == "__main__":
    main()
