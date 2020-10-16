from itertools import permutations
def isPrime(n):
  
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True


def main():
	n = int(input())
	for i in range(n):
		num = input()
		count = 0
		seen = set()
		for i in range(1, len(num) + 1):
			 perms = list(permutations(num, i))
			 for perm in perms:
			 	next = ''.join(perm).strip('0')
			 	if next not in seen:
			 		seen.add(next)
			 		if len(next) != 0:
			 			if isPrime(int(next)):
			 				count += 1
			 

		print(count)



if __name__ == '__main__':
	main()