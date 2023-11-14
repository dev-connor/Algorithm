n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x: # target 이 제일 작은 동전보다 작으면 만들 수 없음
        break
    target += x

print(target)

'''
5
3 2 1 1 9

4
1 2 3 8 
'''