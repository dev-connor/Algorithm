from collections import deque

# +2 - 6:31
def solution(s):
    stack = deque()

    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    array = []
    s1 = "(())()"
    s2 = ")()("
    s3 = "(()("
    result = solution(s3)
    print(result)
