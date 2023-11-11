from collections import deque

def compare(str1, str2):
    cnt = 0

    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            cnt += 1

    return cnt
# +3 27m
def solution(begin, target, words):
    q = deque([(begin, 0, [])])
    while q:
        s, ch, visited = q.popleft()

        if s == target:
            return ch

        for ns in words:
            if compare(s,ns) == 1 and ns not in visited:
                newVisited = visited.copy()
                newVisited.append(ns)
                q.append((ns,ch+1, newVisited))

    return 0

if __name__ == '__main__':
    arrays = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = solution('hit', 'cog', arrays)
    print(result)