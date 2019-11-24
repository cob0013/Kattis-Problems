from sys import stdin, stdout 
def main():
	t = int(stdin.readline().strip())
	for i in range(t):
		n = int(stdin.readline().strip())
		nums = []
		inconsistent = False
		for j in range(n):
			nums.append(stdin.readline().strip())
		nums = sorted(nums)
		print(nums)
		for j in range(n - 1):
			
			if len(nums[j]) < len(nums[j + 1]) and nums[j + 1][:len(nums[j])] == nums[j]:
				inconsistent = True
				break
		if inconsistent:
			print("NO")
		else:
			print("YES")
if __name__ == "__main__":
	main()