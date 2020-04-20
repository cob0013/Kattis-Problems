def main():
    case = 1
    while True:
        try:
            n = int(input())
            print("Case " + str(case) + ":")
            nums = []
            for i in range(n):
                    nums.append(int(input()))
            nums.sort()
            m = int(input())
            for i in range(m):
                    q = int(input())
                    close = closest(nums, q)
                    print("Closest sum to " + str(q) + " is " + str(close) + ".")
            case += 1
        except:
                break

def closest(nums, n):
        output = -1
        bestDiff = 9999999999999
        l = len(nums)
        for i in range(l):
                for j in range(i + 1, l):
                    check = abs(nums[i] + nums[j] - n)
                    if check < bestDiff:
                            bestDiff = check
                            output = nums[i] + nums[j]
        return output
if __name__ == "__main__":
        main()
