n = int(input())
total = 20
yards = 0
tries = 0
line = input().split()
for i in line:
	total += int(i)
	yards += int(i)
	tries += 1
	if yards >= 10:
		yards = 0
		tries = 0
	if tries == 4:
		print("Nothing")
		break
	if total >= 80:
		print("Touchdown")
		break
	if total <= 20:

		print("Safety")
		break






	



