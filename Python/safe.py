from collections import deque

def main():
    pad = []
    for i in range(3):
        pad.append(tuple(map(int, input().split())))
    print(crack(tuple(pad)))

def crack(pad):
    q = deque()
    visited = set()
    visited.add(tuple(pad))
    q.append((pad, 0))

    while q:
        currPad, count = q.popleft()
        for i in range(3):
            for j in range(3):
                next_ = shift(currPad, i, j)
                
                if unlocked(next_):
                    return count + 1
                if next_ not in visited:
                    visited.add(next_)
                    q.append((next_, count + 1))
    return -1

def shift(pad, r, c):
    next_ = [list(x) for x in pad]
    for i in range(3):
        next_[i][c] = (pad[i][c] + 1) % 4
        next_[r][i] = (pad[r][i] + 1) % 4
    return tuple(tuple(a) for a in next_)

def unlocked(pad):
    for i in range(3):
        for j in range(3):
            if pad[i][j] != 0:
                return False

    return True
if __name__ == "__main__":
    main()
