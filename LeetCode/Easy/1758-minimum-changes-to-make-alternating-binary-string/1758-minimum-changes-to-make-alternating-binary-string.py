class Solution:
    def minOperations(self, s: str) -> int:
      cnt = 0
      for i,c in enumerate(s): # 1010
        if i % 2 == 0:
          if c == '0':
            cnt += 1
        else:
          if c == '1':
            cnt += 1
      answer = cnt
      cnt = 0
      for i,c in enumerate(s): # 0101
        if i % 2 == 0:
          if c == '1':
            cnt += 1
        else:
          if c == '0':
            cnt += 1
      answer = min(answer, cnt)

      return answer