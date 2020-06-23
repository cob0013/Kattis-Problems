flip = {2:5, 5:2, 6:9, 9:6, 1:1, 8:8, 0:0}
def convert(n):
     out = ""
     while (n > 0):
        d = n % 10
        if d not in flip:
             return -1
        out += str(d)
        n //= 10
     return int(out)

def main():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    lookingFor = set()
    for num in nums:
            num1 = num
            num2 = convert(num)
            if num1 in lookingFor or num2 in lookingFor:
                    print("YES")
                    return
            lookingFor.add(s - num1)
            lookingFor.add(s - num2)
    print("NO")


if __name__ == "__main__":
        main()
