def calc(ingredients):
	sour = 1
	bitter = 0
	for i in ingredients:
		sour *= i[0]
		bitter += i[1]
	return(abs(sour - bitter))




from itertools import combinations 
n = int(input())
ingredients = []
best = 9999999
for i in range(n):
	s, b = map(int, input().split())
	ingredients.append([s, b])
for i in range(1, n + 1):
	combos = combinations(ingredients, i)
	for l in combos:
		best = min(calc(l), best)

print(best)









