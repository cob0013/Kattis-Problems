from collections import deque 

def main():
	floors, start, goal, u, d = map(int, input().split())
	q = deque()
	visited = set()
	q.append((start, 0))
	visited.add(start)
	while q:
		curr, count = q.popleft()
		if curr == goal:
			print(count)
			break
		up = curr + u
		down = curr - d
		if up <= floors and up not in visited:
			visited.add(up)
			q.append((up, count + 1))
		if down > 0 and down not in visited:
			visited.add(down)
			q.append((down, count + 1))
	else:
		print("use the stairs")

if __name__ == "__main__":
	main() 
