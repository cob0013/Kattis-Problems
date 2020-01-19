def main():
    t = int(input())
    input()
    for i in range(t):
        ccs, ce = map(int, input().split())
        students = []
        while True:
            try:
                line = input()
                if line == "\n":
                    break
                students.append(list(map(int, input().split())))
            except:
                break
        count = 0
        cs = []
        e = []
        for i in range(len(students)):
            for student in students[i]:
                if count < ccs:
                    cs.append(student)
                else:
                    e.append(student)
                count += 1
        csavg = sum(cs) / ccs
        eavg = sum(e) / ce
        output = 0
        for s in cs:
            if s > eavg and s < csavg:
                output += 1
        print(output)
    
if __name__ == "__main__":
    main()

            
        