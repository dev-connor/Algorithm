n = int(input())
def multiple(n):
    if n <= 1:
        return 1

    return n * multiple(n-1)

answer = multiple(n)
print(answer)