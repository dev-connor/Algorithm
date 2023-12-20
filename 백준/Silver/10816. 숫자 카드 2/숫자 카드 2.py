# 3:01
import bisect

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

cards.sort()

for n in nums:
    print(bisect.bisect_right(cards,n) - bisect.bisect_left(cards,n))
