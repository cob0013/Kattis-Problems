from collections import deque

def equals(word1, word2, translations):
	if word1 == (word2):
		return True
	if len(word1) != len(word2):
		return False
	for i in range(len(word1)):
		if word1[i] == word2[i]:
			continue
		if not bfs(word1[i], word2[i], translations):
			return False
	return True

def bfs(c1, c2, translations):
	visited = set()
	visited.add(c1)
	q = [c1]
	while q:
		current = q.pop(0)
		if current not in translations:
			continue
		neibs = translations[current]
		for n in neibs:
			if n not in visited:
				visited.add(n)
				q.append(n)
			if n == c2:
				return True
	return False









def main():
	m, n = map(int, input().split())
	translations = {}
	for i in range(m):
		letter, translation = input().split()
		if letter not in translations:
			translations[letter] = set()
		translations[letter].add(translation)
	for i in range(n):
		word1, word2 = input().split()
		if equals(word1, word2, translations):
		 	print("yes")
		else:
		 	print("no")



if __name__ == '__main__':
	main()