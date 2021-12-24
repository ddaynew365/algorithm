def solution(str1, str2):
    set1:dict[str:int] = dict()
    list1:list[str] = list(str1.lower())
    list2:list[str] = list(str2.lower())
    for i in range(1,len(list1)):
        two_sum = list1[i-1] + list1[i]
        if two_sum.isalpha():
            if two_sum in set1:
                set1[two_sum][0] +=1
            else:
                set1[two_sum] = [1,0]
    
    for i in range(1, len(list2)):
        two_sum = list2[i-1] + list2[i]
        if two_sum.isalpha():
            if two_sum in set1:
                set1[two_sum][1] += 1
            else:
                set1[two_sum] = [0,1]
    inter = 0
    union = 0
    for a,b in set1.values():
        inter += min(a,b)
        union += max(a,b)
    if union == 0: 
        return 65536
    else:
        return int(inter / union * 65536)