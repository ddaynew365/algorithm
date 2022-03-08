from collections import Counter
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        result = 0
        
        while True:
            sub_count = 0
            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1
                # counter 개수 -1
                counter.subtract(task)
                # counter 0 이하 목록 삭제
                counter += Counter()
                
            if not counter:
                break
            
            result += n - sub_count + 1
        return result