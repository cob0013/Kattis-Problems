def avg(lst):
	return sum(lst) / len(lst)
def main():
	t = int(input())
	for i in range(t):
		blank = input()
		cs, e = map(int, input().split())
		csList = list(map(int, input().split()))
		eList = list(map(int, input().split()))
		csAvg = avg(csList)
		eAvg = avg(eList)
		count = 0
		for student in csList:
			if student < csAvg and student > eAvg:
				count += 1
		print(count)

		
if __name__ == "__main__":
	main()