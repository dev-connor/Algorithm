# +4 - 25:38
def solution(tickets):
    answer = []
    visited = [False] * len(tickets)

    def dfs(cnt, now, routes):

        if cnt == len(tickets):
            answer.append(routes.copy())

        for i,t in enumerate(tickets):
            start = t[0]
            to = t[1]
            if now == start and not visited[i]:
                visited[i] = True
                routes.append(to)
                dfs(cnt + 1, to, routes)
                routes.pop()
                visited[i] = False

    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            start = i
            visited[start] = True
            dfs(1, tickets[start][1], [tickets[start][0],tickets[start][1]])
            visited[start] = False

    answer.sort()
    return answer[0]

array1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
array2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
result = solution(array2)
print(result)
