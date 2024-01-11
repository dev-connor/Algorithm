def recursion(s, l, r, cnt):
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: return recursion(s, l+1, r-1, cnt+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

t = int(input())
for _ in range(t):
    a,b= isPalindrome(input())
    print(a,b)
# print(isPalindrome("ABBA")) # 1
# print(isPalindrome("ABC"))   # 0