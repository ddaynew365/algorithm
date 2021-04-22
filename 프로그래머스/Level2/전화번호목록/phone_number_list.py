
"""
1. 단순하게 이중 for문을 사용 - 정확도는 만점이었으나 효율성 부분에서 0점
"""

def solution(phone_book):
    answer = True
    
    for i in range(len(phone_book)):
        length1 = len(phone_book[i])
                   
        for j in range(i+1, len(phone_book)):
            length2 = len(phone_book[j])       
            
            if phone_book[i] == phone_book[j][:length1] or phone_book[j] == phone_book[i][:length2] :
                answer = False
                break
                   
    return answer
    

"""
2. 처음에 문자열을 사전순서로 정렬을 하여 해당 인덱스의 값과 그 다음의 인덱스값만을 비교해도 되게 코드를 구성하였다. 이에 따라 for문을 중첩하지 않아도 되어 
점수는 만점을 받았다
"""

    
    def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        length = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:length]:
            answer = False
            break
            
    return answer

"""
3. 아래서부터는 다른 사람의 풀이를 가져온 것이다. 이 분은 zip함수를 사용하였고 startswith()함수를 사용하였다. startswith() 함수는 p1이 p2의 접두어로 존재하는지 확인해주는
함수이다. 이런 함수가 있는지 몰랐던 나는 충격적이었다.
"""
   
    
    
    def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
    

"""
4. 이 분은 해쉬함수를 사용하여 문제를 해결했다. 키에 문자열을, 값에 1을 넣어 초기화시킨 후 temp라는 빈 문자열을 생성하여 문자를 하나씩 넣으며 비교하는 것을 반복하였다.
"""

    

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
