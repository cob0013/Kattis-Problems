# https://open.kattis.com/problems/yinyangstones


def check(t):
	return t[0] == 2*t[1]

def func(s, c):
	return [len(s), s.count(c)]

if check(func(input(), "W")):
	print(1)
else:
	print(0)






