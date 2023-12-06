import heapq

n = int(input())
inputs = list(map(int, input().split()))

inputs.sort()

answer = []
f = 0
e = n-1

while f < e:
    sum_v = inputs[f] + inputs[e]
    heapq.heappush(answer,(abs(sum_v),inputs[f],inputs[e]))
    if sum_v == 0:
        print(inputs[f],inputs[e])
        exit()
    elif sum_v < 0:
        f += 1
    else:
        e -= 1

s,n1,n2 = heapq.heappop(answer)
print(n1,n2)