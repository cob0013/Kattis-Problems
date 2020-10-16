n = int(input())
nums = []
for i in range(n):
    x, p = input().split()
    nums.append(float(p))
nums.sort(reverse  = True)
mult = 1
out = 0
for num in nums:
    out += num * mult
    mult += 1
print(out)
        

