def main():
    while 1:
        n = int(input())
        if n == 0:
            return
        bits = ["?" for i in range(32)]
        for _ in range(n):
            instruction = input().split()
            cmd = instruction.pop(0)
            if cmd == "CLEAR":
                bits[int(instruction[0])] = "0"
            elif cmd == "SET":
                bits[int(instruction[0])] = "1"
            elif cmd == "OR":
                i, j = map(int, instruction)
                if bits[j] == "1" or bits[i] == "1":
                    bits[i] = "1"
                elif bits[j] == "?" or bits[i] == "?":
                    bits[i] = "?"
                else:
                    bits[i] = "0"
            else:
                i, j = map(int, instruction)
                if bits[j] == "0" or bits[i] == "0":
                    bits[i] = "0"
                elif bits[j] == "?" or bits[i] == "?":
                    bits[i] = "?"
                else:
                    bits[i] = "1"
        print("".join(bits[::-1]))
if __name__ == "__main__":
    main()
