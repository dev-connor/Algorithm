# 단순 DFS 로 풀었지만, 백트래킹으로 풀 수 있음
def solution(numbers, target):
    visited = [False] * len(numbers)

    def dfs(count, sum, answer):
        if count == len(numbers):
            if sum == target:
                answer = answer+ 1
            return answer

        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                count +=1
                sum += numbers[i]
                answer =dfs(count, sum, answer)
                sum -= 2*numbers[i]
                answer =dfs(count, sum, answer)

                visited[i] = False
                count -=1
                sum += numbers[i]
                return answer

    answer = dfs(0, 0, 0)

    return answer

if __name__ == '__main__':
    arr = [4, 1, 2, 1]
    result = solution(arr, 4)
    print(result)
