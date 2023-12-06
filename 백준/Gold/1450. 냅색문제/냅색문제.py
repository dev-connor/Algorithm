import sys, math
import itertools
input = sys.stdin.readline

def findSub(arr):
    sub = []
    for select in range(len(arr)+1):
        pool = map(sum, itertools.combinations(arr, select))
        for p in pool:
            if p <= C:
                sub.append(p)
    return sub
    
def getPair(arr, item):
    if item > C:
        return 0
    
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        target = arr[mid] + item
        
        if target <= C:
            start = mid + 1
        else:
            end = mid - 1
    
    return start
    

N, C = map(int, input().split())
weights = list(map(int, input().split()))
count = 0

div = N//2
w_subA = weights[:div]
w_subB = weights[div:]

subsum_a = findSub(w_subA)
subsum_b = findSub(w_subB)

subsum_a.sort()

for b in subsum_b:
    count += getPair(subsum_a, b)

print(count)