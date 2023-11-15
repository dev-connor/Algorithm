import heapq

# +5
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length # 먹기위해 사용한 시간
        length -= 1 # 한 음식을 다 먹었으므로 1을 뺀다
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]

arr1 = [3,1,2]
arr2 = [8,4,6]
answer = solution(arr2, 15)
print(answer)