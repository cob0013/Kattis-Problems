def main():
	conversion = input().split()
	amount = int(conversion[0])
	start = conversion[1][:2]
	end = conversion[3][:2]
	imperial = {}
	imperial["th"] = (0, 1)
	imperial["in"] = (1, 1000)
	imperial["ft"] = (2, 12 * imperial["in"][1])
	imperial["fo"] = (2, 12 * imperial["in"][1])
	imperial["ya"] = (3, 3 * imperial["ft"][1])
	imperial["yd"] = (3, 3 * imperial["ft"][1])
	imperial["ch"] = (4, 22 * imperial["yd"][1])
	imperial["fu"] = (5, 10 * imperial["ch"][1])
	imperial["mi"] = (6, 8 * imperial["fu"][1])
	imperial["le"] = (7, 3 * imperial["mi"][1])

	base = imperial[start][1] * amount
	if amount == 0:
		print(0)
	else:
		print(base / imperial[end][1])







if __name__ == "__main__":
	main()