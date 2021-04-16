# 처음 코드 - 실패
"""
원인: for문 블럭 안에 있는 elif문의 조건에서 len(list) ==1이 문제였다. 처음에 코드를 구상하였을 때는 2개 이상의 인형이 바구니에 있어야만 같은 인형이 생길줄 알아서 적은 코드였다.
      하지만 1개의 인형만 있을 때 같은 인형이 들어오면 터진다는 생각을 미처 못했다. 시간에 쫒겨 초조한 마음으로 인한 코드 구상 단계의 실수가 이런 결과를 가져왔다. 코드 구상 단계가
      코딩에서 가장 중요한 만크 좀 더 여유롭게 생각하는 습관을 가져야겠다.
"""


def solution(board, moves):
    answer = 0
    list =[]
    
    for i in moves:
        
        for j in range(len(board)):
            
            if board[j][i-1] == 0:
                continue
                
            elif len(list) ==0 or len(list) ==1:
                list.append(board[j][i-1])
                board[j][i-1] = 0
                break
                
            else:
                list.append(board[j][i-1])
                board[j][i-1] = 0
                if list[-1] == list[-2]:
                    del list[-1]
                    del list[-1]
                    answer += 2
                break
            
    return answer
    
    
# 성공 코드

def solution(board, moves):
    answer = 0
    list =[]
    
    for i in moves:
        
        for j in range(len(board)):
            
            if board[j][i-1] == 0:
                continue
                
            elif len(list) ==0:
                list.append(board[j][i-1])
                board[j][i-1] = 0
                break
                
            else:
                list.append(board[j][i-1])
                board[j][i-1] = 0
                if list[-1] == list[-2]:
                    del list[-1]
                    del list[-1]
                    answer += 2
                break
            
    return answer
