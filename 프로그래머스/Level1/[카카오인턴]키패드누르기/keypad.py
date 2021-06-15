def solution(numbers, hand):
    answer = []
    keypad ={1:[0,0],
            2: [0,1],
            3: [0,2],
            4: [1,0],
            5: [1,1],
            6: [1,2],
            7: [2,0],
            8: [2,1],
            9: [2,2],
            '*': [3,0],
             0: [3,1],
            '#': [3,2]}

    le = '*'
    ri = '#'
    
    for idx, val in enumerate(numbers):
        if val == 1 or val == 4 or val ==7 or val == '*':
            answer.append('L')
            le = val
            
        elif val == 3 or val ==6 or val==9 or val == '#':
            answer.append('R')
            ri = val
            
        else:
            le_distance = abs(keypad[val][0] - keypad[le][0]) + abs(keypad[val][1] - keypad[le][1])
            ri_distance = abs(keypad[val][0] - keypad[ri][0]) + abs(keypad[val][1] - keypad[ri][1])
            
            if ri_distance > le_distance:
                answer.append('L')
                le = val
            elif ri_distance < le_distance:
                answer.append('R')
                ri= val
            else:
                if hand == 'left':
                    answer.append('L')
                    le = val 
                elif hand == 'right':
                    answer.append('R')
                    ri = val     
    
    answer = ''.join(answer)
    return answer
