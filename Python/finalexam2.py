def main():
    n = int(input())
    correct = []
    put = []
    for i in range(n):
        answer = input()
        correct.append(answer)
        put.append(answer)
    put.pop(0)
    count = 0
    for i in range(n - 1):
        if correct[i] == put[i]:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
