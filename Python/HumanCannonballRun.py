def distance():

def main():
	start = list(map(float, input().split()))
	finish = list(map(float, input().split()))
	cannons = []
	n = int(input())
	for i in range(n):
		cannons.append(list(map(float, input().split())))
	print(cannons)
if __name__ == '__main__':
	main()
	##not finished