array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]: # 왼쪽에서 큰 값 찾기
            left += 1
        while right > start and array[right] >= array[pivot]: # 오른쪽에서 작은 값 찾기
            right -= 1
        if left > right: # 엇갈렸다면
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array,start,right - 1)
    quick_sort(array,right + 1, end)

quick_sort(array,0,len(array) - 1)
print(array)