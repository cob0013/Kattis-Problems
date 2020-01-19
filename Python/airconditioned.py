   
    

def main():
    n = int(input())
    minions = []
    for i in range(n):
        l, u = map(int, input().split())
        minions.append((u,l ))
    minions.sort()
    rooms = set()
    for m in minions:
        fits = False
        for i in range(m[1], m[0] + 1):
            if i in rooms:
                fits = True
                break
        if not fits:
            rooms.add(m[0])
    print(len(rooms))
    

        




if __name__ == "__main__":
    main()
