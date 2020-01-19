# dp probelm
# not finished
def util(maxCapacity, weights, vals, n):

	if n == 0 or maxCapacity == 0:
		return 0

	if weights[n - 1] > maxCapacity:
		return util(maxCapacity, weights, vals, n)

	else:
		return max(vals[n - 1] + util(maxCapacity - weights[n - 1], weights, vals, n - 1), 
			util(maxCapacity, weights, vals, n - 1 ))



def main():
	while True:
			c, n = map(int, input().split())
			weights = []
			vals = []
			for i in range(n):
				v, w = map(int, input().split())
				vals.append(v)
				weights.append(w)
			print(util(c, weights, vals, n))

if __name__ == "__main__":
	main()