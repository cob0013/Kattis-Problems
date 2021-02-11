def main():
    n, k = map(int, input().split())
    cmds = input().split()
    stack = []
    curr_position = 0
    for cmd in cmds:
        if cmd == "undo":
            curr_position = stack.pop()
        else:
            curr_position = (curr_position + int(cmd)) % k
            while curr_position < 0:
                curr_position += k
            stack.append(curr_position)
            
    print(curr_position)


if __name__ == "__main__":
    main()
