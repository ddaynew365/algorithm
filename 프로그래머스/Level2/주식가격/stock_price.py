
"""
1. 단순하게 이중 for문을 사용 - 정확도는 만점이었으나 효율성 부분에서 0점
"""


def solution(prices):
    answer = []
    for cho, val in enumerate(prices):
        time = len(prices) - (cho +1)
        
        for com_cho, com_val in enumerate(prices):
            if cho >= com_cho:
                continue
                
            if val > com_val:
                time = com_cho - cho
                break
                
        answer.append(time)
    return answer
    

"""
2. 단순하게 이중 for문을 사용하였으나 enumerate대신 range로 for문을 돌렸다 - 만점을 받았으나 시간 복잡도가 그대로 O(n^2)이라서 맘에 드는 코드는 아니었다.
"""


def solution(prices):
    answer = []
    for cho, val in enumerate(prices):
        time = len(prices) - (cho +1)
        
        for com_cho in range(cho+1, len(prices)):
                
            if val > prices[com_cho]:
                time = com_cho - cho
                break
                
        answer.append(time)
    return answer
    

"""
3. 구글링을 해보니 사람들은 pythontic한 range보다 enumerate를 사용하는 것이 좋다라고 하였다. 그래서 코드1과 코드2의 차이점인 내부 for문의 시작점을 생각하여
enumerate함수를 사용하여 내부 for문의 시작점을 외부 for문의 인덱스 +1 로 수정해보았다. 하지만 결과는 효율성 0점이었다. 아마 내 생각으로는 slice하는 과정에서
발생하는 연산때문이라고 생각한다. 하지만 enumerate함수를 사용한 for문을 중간에서부터 시작시키는 방법이 slice외에는 떠오르지가 않는다.
"""


def solution(prices):
    answer = []
    for cho, val in enumerate(prices):
        time = len(prices) - (cho +1)

        for com_cho, com_val in enumerate(prices[cho+1:]):
            com_cho = cho + com_cho+1
            if val > com_val:
                time = com_cho - cho
                break
                
        answer.append(time)
    return answer
    

 """
 4. 자료구조 stack을 사용 - 처음에 스택으로 구현하려했으나 어려워 포기했었는데 스택에 값이 아닌 인덱스를 넣는 방식을 사용하니 수월하게 구현할 수 있었다.
 """


def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    for i in range(1, len(prices)):
        if prices[i] < prices[stack[-1]]:
            for j in stack[::-1]:
                if prices[i] < prices[j]:
                    answer[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        answer[stack[i]] = len(prices) - stack[i] - 1
    return answer

"""
5. 4/ 28 재 풀이: 다시 한번 스택으로 도전해 보았다. 하지만 결과는 실패였다. 제공해준 테스트 케이스는 합격을 받았지만 히든 케이스에 의해 실패가 떴다. 여러 테스트케이스를 추가해 확인한
결과 스택에서 여러개가 동시에 빠지는 경우를 생각하지 못한 것이 문제였다. 이미 한번 풀었던 문제를 실패했다는 것에 부족함을 느꼈다. 앞으로는 새로운 문제뿐만 아니라 복습 역시 꾸준히 

"""

def solution(prices):
    #스택 사용 - 리스트 
    #스택 맨위와 들어올 수를 비교 -> 맨위가 크면 맨위를 뺴내고 시간계산/ 들어올 수가 크면 넣는다
    answer = [-1] * len(prices)
    stack =[]
    for put in range(len(prices)):

        
        if not stack:
            stack.append(put)
            
        else:
            top = stack.pop()
            
            while prices[top] > prices[put]:
                answer[top] = put - top
                if len(stack) == 0:
                    break
                top = stack.pop() 
            if prices[top] <= prices[put]:
                stack.append(top)   
            stack.append(put)  
        
    while stack:
        top = stack.pop()
        answer[top] = len(prices) -top -1

    return answer
