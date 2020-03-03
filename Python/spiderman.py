from collections import deque 
def main():

    #not fast enough learn dp
    n = int(input())
    for i in range(n):
        l = int(input())
        distances = list(map(int, input().split()))
        q = []
        q.append((0, 0, 0, ""))
        works = []
        while q:
            index, currentheight, maxheight, path = q.pop(0)
            if index == l and currentheight == 0:
                works.append((maxheight, path))
                continue
            if index == l:
                continue
            
            if currentheight - distances[index] >= 0:                
                q.append((index + 1, currentheight - distances[index], maxheight, path + "D"))
            q.append((index + 1, currentheight + distances[index],
                max(maxheight, currentheight + distances[index]), path + "U"))
            
        works.sort()
        if works:
            print(works[0][1])
        else:
            print("IMPOSSIBLE")



if __name__ == "__main__":
    main()
