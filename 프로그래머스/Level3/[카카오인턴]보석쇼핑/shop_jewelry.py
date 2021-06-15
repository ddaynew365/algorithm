# 처음 풀이-> 슬라이딩 윈도우 알고리즘을 사용하였다. 정확도는 모두 맞았지만 효율성에서 0점을 맞았다. 시간 복잡도를 줄일 필요가 있었다.
def solution(gems):
    answer = []
    kind = len(set(gems))
    
    final_low = 0
    final_high = 100000
    
    for low in range(len(gems)):
        path = False
        count_dict ={}
        
        for high in range(low,len(gems)):
            if gems[high] not in count_dict.keys():
                count_dict[gems[high]] = 1
            else:
                count_dict[gems[high]] += 1
                
            if len(set(count_dict.keys())) == kind:
                path = True
                if high-low < final_high - final_low:
                    final_high = high
                    final_low = low
                break
        
        if path == False:
            break
            
    answer = [final_low+1, final_high+1]
    return answer
# 2번째 풀이 -> count_dict를 새로 초기화하고 처음부터 값을 다시 집어넣는 행위는 시간복잡도를 크게 높이므로 기존의 count_dict에서 빠진 gems[low]와 gems[high]만 빼내는 방법을
#               사용하였다. gems[high]를 뺴낸 이유는 [ 'XYZ', 'XYZ', 'XYZ] 와 같은 경우를 해결하기 위해서이다. 하지만 이걸로는 효율성 점수를 만족하지 못하였다.
def solution(gems):
    answer = []
    kind = len(set(gems))
    
    final_low = 0
    final_high = 100000
    pathnext = 0
    count_dict ={}
    
    for low in range(len(gems)):
        path = False
    
        for high in range(pathnext,len(gems)):
            if gems[high] not in count_dict.keys():
                count_dict[gems[high]] = 1
            else:
                count_dict[gems[high]] += 1
                
            if len(set(count_dict.keys())) == kind:
                path = True
                pathnext = high
                if abs(high-low) < abs(final_high - final_low):
                    final_high = high
                    final_low = low
                break
        
        if path == False:
            break
            
        if gems[low] in count_dict.keys():
            if count_dict[gems[low]] == 1:
                del count_dict[gems[low]]
            else:
                count_dict[gems[low]] -= 1

        if gems[high] in count_dict.keys():
            if count_dict[gems[high]] == 1:
                del count_dict[gems[high]]
            else:
                count_dict[gems[high]] -= 1
            
    answer = [final_low+1, final_high+1]
    return answer
  
# 마지막 푸이 -> 집합 set을 매번 새로 만드는 것도 시간적복잡도를 크게 키운다고 생각하여 count_set이라는 변수에 집합을 넣어줘 조금만 변하도록 조정하였다. 결과적으로 정확성, 효율성
#               모두 성공을 얻어냈다.
def solution(gems):
    answer = []
    kind = len(set(gems))
    
    final_low = 0
    final_high = 100000
    pathnext = 0
    count_dict ={}
    count_set = set()
    
    for low in range(len(gems)):
        path = False
    
        for high in range(pathnext,len(gems)):
            if gems[high] not in count_dict.keys():
                count_dict[gems[high]] = 1
                count_set.add(gems[high])
            else:
                count_dict[gems[high]] += 1
                
            if len(count_set) == kind:
                path = True
                pathnext = high
                if abs(high-low) < abs(final_high - final_low):
                    final_high = high
                    final_low = low
                break
        
        if path == False:
            break
            
        if gems[low] in count_dict.keys():
            if count_dict[gems[low]] == 1:
                del count_dict[gems[low]]
                count_set.remove(gems[low])
            else:
                count_dict[gems[low]] -= 1

        if gems[high] in count_dict.keys():
            if count_dict[gems[high]] == 1:
                del count_dict[gems[high]]
                count_set.remove(gems[high])
            else:
                count_dict[gems[high]] -= 1
            
    answer = [final_low+1, final_high+1]
    return answer
