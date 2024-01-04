n = int(input())
have = set(map(int,input().split()))
m = int(input())
cards = list(map(int,input().split()))

answer = []
for card in cards:
    if card in have:
        answer.append(1)
    else:
        answer.append(0)
for i in answer:
    print(i,end=' ')
        