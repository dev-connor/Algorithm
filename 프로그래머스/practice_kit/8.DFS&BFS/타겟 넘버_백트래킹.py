def solution(numbers, target):
    arr = []

    def dfs(count):
        answer = 0
        if count == len(numbers):
            newArr = [x*y for x,y in zip(numbers,arr)]
            if sum(newArr) == target:
                return 1
            return 0

        for i in range(2):
            if i % 2 == 0:
                arr.append(1)
                answer += dfs(count+1)
                arr.pop()
            else:
                arr.append(-1)
                answer += dfs(count+1)
                arr.pop()
        return answer

    answer = dfs(0)

    return answer

if __name__ == '__main__':
    arrays = [4, 1, 2, 1]
    result = solution(arrays, 4)
    print(result)