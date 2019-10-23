tc = int(input())
for i in range(tc):
	number = raw_input().split()
	ng = number[0]
	nm = number[1]
	ngTotal = int(raw_input()) * int(ng)
	nmTotal = int(raw_input()) * int(nm)
	if ngTotal > nmTotal:
		print("Godzilla")
	else:
		print("MechaGodzilla")