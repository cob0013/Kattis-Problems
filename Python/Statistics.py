
def main():
	count = 1
	while True:
		try:
			line = list(map(int, input().split()))
			nums = line[1::]
			nums.sort()
			print("Case", str(count) +  ":", nums[0], nums[-1], nums[-1] - nums[0])
			count += 1
		except:
			break
		

if __name__ == "__main__":
	main()