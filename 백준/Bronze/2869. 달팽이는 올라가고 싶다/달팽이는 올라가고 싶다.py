import math

a,b,v = map(int, input().split())
target = v-a
date = math.ceil(target / (a-b))
print(date + 1)