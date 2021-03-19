def main():
    n = int(input())
    side_lengths = []
    for i in range(n):
        side_lengths.append(int(input()))
    count = 0
    trips = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if check(side_lengths[i], side_lengths[j], side_lengths[k]):
                    trips.add(set((side_lengths[i], side_lengths[j], side_lengths[k])))

    print(trips)


def check(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    return True


main()
