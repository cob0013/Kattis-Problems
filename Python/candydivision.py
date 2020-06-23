from math import ceil
def factors(n):
    out = set()
    for i in range(1, ceil(n ** .5) + 1):
        if n % i == 0:
            out.add(i - 1)
            out.add(n // i - 1)
    return list(out)

def main():
    n = int(input())
    
    print(" ".join(list(map(str, sorted(factors(n))))))

if __name__ == "__main__":
    main()
