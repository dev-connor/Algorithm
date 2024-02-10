import math

s = input()
arr = list(s)
line = math.ceil(len(arr)/10)

for i in range(line):
    split = ''.join(arr[10*i:10*i+10])
    print(split)