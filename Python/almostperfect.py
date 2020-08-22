from functools import reduce

def factors(n):    
    out = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    out.remove(n)
    return out
def main():
    while True:
            try:
                n = int(input())
                fax = factors(n)
                if abs(sum(fax) - n) == 0:
                    print(n, "perfect")
                elif abs(sum(fax) - n) <= 2:
                    print(n, "almost perfect")
                else:
                    print(n, "not perfect")
            except:
                    break


if __name__ == "__main__":
        main()
