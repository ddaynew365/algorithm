def next_num(num):
    if num % 2 == 0:
        return num // 2
    else:
        return (num // 2 )+ 1

def is_fight(num1, num2):
    num1 -= 1
    num2 -= 1
    if num1 // 2 == num2 // 2:
        return True
    else:
        return False
    
def solution(n,a,b):
    count = 1
    while True:
        if is_fight(a,b):
            return count
        else:
            count += 1
            a, b = next_num(a), next_num(b)
                       
    return answer