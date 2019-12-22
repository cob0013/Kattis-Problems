def main():
	n = int(input())
	dom = {}
	kattis = {}
	count = 0
	for i in range(n):
		ans = input()
		if ans in dom:
			dom[ans] = dom[ans] + 1
		else:
			dom[ans] = 1
	for i in range(n):
		ans = input()
		if ans in kattis:
			kattis[ans] = kattis[ans] + 1
		else:
			kattis[ans] = 1
	for key in kattis:
		if key in dom:
			count += min(kattis[key], dom[key])
	print(count)


if __name__ == "__main__":
	main()