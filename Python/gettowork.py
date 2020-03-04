def main():
    c = int(input())
    for i in range(c):
        n, t = list(map(int, input().split()))
        e = int(input())
        towns = {}
        for j in range(e):
            h, p = list(map(int, input().split()))
            if h == t:
                continue

            if h not in towns:
                towns[h] = [p]
            else:
                towns[h].append(p)
        output = "Case #" + str(i + 1) + ": "
        for j in range(1, n + 1):      
            works = True
            if j in towns:
                
               people = len(towns[j])
               capacity = sum(towns[j])
               sort = sorted(towns[j])
               if capacity < people:
                 works = False
                 break
               count = 0
            
               while people > 0 and sort[-1] != 0: 
                  people -= sort.pop()
                  count += 1
                               
            
               output += " " + str(count)
            else:
                output += " " + str(0)
        if works:
            print(output)
        else:
            print("Case #" + str(i + 1) + ": IMPOSSIBLE")



if __name__ == "__main__":
    main()
