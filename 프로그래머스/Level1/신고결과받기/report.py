from collections import defaultdict
from typing import List

def solution(id_list: List[str], report: List[str], k: int) -> List[int]:
    answer: List[int] = list()
    warn_num, warn_list = defaultdict(int), defaultdict(list)
    report: List[str] = list(set(report))
    
    for log in report:
        do: str
        did: str
        do, did = log.split(" ")
        warn_num[did] += 1
        warn_list[do].append(did)
        
    for do in id_list:
        if do not in warn_list:
            answer.append(0)
        else:
            count: int
            count = len([x for x in warn_list[do] if warn_num[x] >= k])
            answer.append(count)
    return answer