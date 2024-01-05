# 8:41
from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        answer = 0
        counts = []

        for line in bank:
            count = line.count('1')
            if count != 0:
                counts.append(count)
        
        if len(counts) == 0:
            return 0 
        
        before = counts[0]
        for i in range(1,len(counts)):
            answer += before*counts[i]
            before = counts[i]

        return answer