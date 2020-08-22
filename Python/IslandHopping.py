import math
import heapq
def distance(p1, p2):
	return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))




# prims

def prim(pts, n):
	mst = set()
	cost = 0
	pq =  [(0, 0)]
	distances = [1000000] * n
	mst_count = 0
	while mst_count < n and pq:
		weight, vert = heapq.heappop(pq)
		if vert in mst:
			continue
		mst.add(vert)
		cost += weight
		mst_count += 1
		for neigh in range(n):
			if vert == neigh or neigh in mst:
				continue
			dist = distance(pts[vert], pts[neigh])
			if dist > distances[neigh]:
				continue
			distances[neigh] = dist
			heapq.heappush(pq, (dist, neigh))

	return cost


def main():
	n = int(input())
	for i in range(n):
		m = int(input())
		islands = []
		for i in range(m):
			x, y = map(float, input().split())
			islands.append((x, y))
		print(prim(islands, m))



if __name__ == "__main__":
	main()
