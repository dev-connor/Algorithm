import heapq
import math

n = int(input())
nums = list(map(int, input().split()))

answer = []
graph = [[] for i in range(n)]
indegree = [0] * (n)

for i in range(n):
    for j in range(i+1,n):
        if math.gcd(nums[i],nums[j]) != 1:
            graph[i].append(j)
            indegree[j] += 1

def topology_sort():
    h = []

    for i in range(0, n): # 진입차수가 0인 노드를 큐에 삽입
        if indegree[i] == 0:
            heapq.heappush(h,(nums[i],i))

    for i in range(n):
        now = heapq.heappop(h)
        answer.append(now[0])

        for i in graph[now[1]]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(h, (nums[i], i))
    else:
        print(' '.join(map(str, answer)))

topology_sort()
