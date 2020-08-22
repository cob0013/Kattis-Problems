def primes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):

                for i in range(p * p, n + 1, p):
                    prime[i] = False
        p += 1

    primes = {p for p in range(2, n + 1) if prime[p]}
    return primes
def main():
    _primes = primes(32001)
    n = int(input())
    for i in range(n):
        x = int(input())
        count = 0
        out = []
        for j in range(x // 2 + 1):
            if j in _primes and x - j in _primes:
                out.append("{}+{}".format(j, x - j))
                count += 1
        print("{} has {} representation(s)".format(x, count))
        print("\n".join(out))
        print()

if __name__ == "__main__":
    main()
