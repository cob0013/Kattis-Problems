def main():
	n, m = map(int, input().split())
	songs = []
	for i in range(1, n + 1):
		fi, name = input().split()
		fi = int(fi)
		q = fi * (i)
		# added n+ 1 - i to handle tying by index when sorting
		songs.append((q, n + 1 - i, name))

	songs.sort(reverse = True)
	for i in range(m):
		print(songs[i][2])


if __name__ == '__main__':
	main()