import math

n = int(input())

array = [True for i in range(n+1)] # True 일 때 소수
array[0] = array[1] = False
primes = []

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i,b in enumerate(array):
    if b:
        primes.append(i)

count = 0
interval_sum = 0
end = 0

length = len(primes)
for start in range(length):
    while interval_sum < n and end < length:
        interval_sum += primes[end]
        end += 1
    if interval_sum == n:
        count += 1
    interval_sum -= primes[start]

print(count)