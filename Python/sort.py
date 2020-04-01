def main():
        n, c = map(int, input().split())
        line = list(map(int, input().split()))
        count = dict()
        index = dict()
        
        for i in range(len(line)):
                if line[i] in count:
                        count[line[i]] += 1
                else:
                        count[line[i]] = 1
                        index[line[i]] = -i
        nums = []
       
        for key, val in count.items():
                 nums.append((val,index[key], key))
        nums.sort(reverse = True)
        output = []
        for n in nums:
                for i in range(n[0]):
                    output.append(str(n[2]))
        print(" ".join(output))
if __name__ == "__main__":
        main()
