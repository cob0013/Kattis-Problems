def main():
    words = dict()
    count = dict()
    n = int(input())
    said_by_all = set()
    for i in range(n):
        message = input().split()
        name = message.pop(0)
        if name not in words:
            words[name] = set()
        for word in message:
            said_by_all.add(word)
            words[name].add(word)
            if word not in count:
                count[word] = 0
            count[word] += 1
    output = []
    for w in words.values():
       said_by_all = w & said_by_all
    for w in said_by_all:
        output.append((-count[w], w))
    output.sort()
    if output:
        for out in output:
            print(out[1])
    else:
        print("ALL CLEAR")
if __name__ == "__main__":
    main()
