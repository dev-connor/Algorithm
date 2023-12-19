n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

arr1.sort()
for i in arr2:
    if binary_search(arr1, i, 0, len(arr1)-1):
        print(1)
    else:
        print(0)