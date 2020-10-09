def LIS(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)
def LDS(arr):
    n = len(arr)
    lds = [1] * n
    for i in range(1, n):
        for j in range(i):
            if (arr[i] < arr[j] and 
                    lds[i] < lds[j] + j):
                    lds[i] =  lds + 1
    return max(lds)


def main():
    n = int(input())
    trains = []
    for i in range(n):
        trains.append(int(input()))
    print(max(LDS(trains), LIS(trains)))



if __name__ == "__main__":
    main()
