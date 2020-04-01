def main():
    l, h = map(int, input().split())
    count = 0
    for i in range(l, h + 1):
       if "0" in str(i):
           continue
       if works(str(i)):
           count += 1
    print(count)

def works(n):
    seen = set()
    for i in map(int, n):
      
        if int(n) % i != 0 or i in seen:
            return False
        seen.add(i)
    return True
if __name__ == "__main__":
    main()

