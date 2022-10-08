def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid +1
    return None

n = int(input())
array = list(map(int, input().split()))

array.sort()

m = int(input())
array_2 = list(map(int, input().split()))

for i in array_2:
    x = binary_search(array, i, 0, n -1)
    if x != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
