def main():
	h, w, n = map(int, input().split())
	bricks = map(int, input().split())
	currentwidth = 0
	currentheight = 0
	for brick in bricks:
		currentwidth += brick
		if currentwidth > w:
			print("NO")
			return
		if currentwidth == w:
			currentheight += 1
			if currentheight == h:
				break
			currentwidth = 0
	if currentwidth == w and h == currentheight:
		print("YES")



if __name__ == "__main__":
	main()