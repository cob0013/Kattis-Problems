def main():
	t = int(input())
	for i in range(t):
		blank = input()
		ng, nm = map(int, input().split())
		sg = list(map(int, input().split()))
		smg = list(map(int, input().split()))
		sg.sort(reverse = True)
		smg.sort(reverse = True)

		while sg and smg:
			if sg[len(sg) - 1] == smg[len(smg) - 1]:
				smg.pop()
				if not sg or  not smg:
					break
			if sg[len(sg) - 1] < smg[len(smg) - 1]:
				sg.pop()
				if not sg or not smg:
					break
				
			else:
				smg.pop()
		if smg:
			print("MechaGodzilla")
		else:
			print("Godzilla")
				

if __name__ == '__main__':
	main()