"""
첫 번째 풀이에는 함수를 모두 구현하였음에도 중구난방식이라 어디가 어느 기능을 담당하는지 한눈에 보기 힘들었다. 하지만 각각의 기능을 모두 함수로 바꿔 표현하니
훨씬 간단해 보이는 것을 느꼈다.
"""
'''
첫번째 풀이
'''
def recom(new_id):
    #1
    new_id = new_id.lower()
    #2
    for i in new_id:
        if i.islower() == False and i != '-' and i != '_' and i != '.' and i.isnumeric() == False:
            new_id = new_id.replace(i,'')
    #3
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    #4
    if new_id.startswith('.') == True:
        new_id = new_id[1:]
    
    if new_id.endswith('.') == True:
        new_id = new_id[:len(new_id)-1]
    #5   
    if new_id == "":
        new_id += "a"
    #6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id.endswith('.') == True:
            new_id =new_id[:len(new_id)-1]
    #7
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1]*(3-len(new_id))
        
    return new_id

def solution(new_id):
    answer = new_id
    if len(new_id) < 3 or len(new_id) > 15:
        return recom(new_id)
    
    for i in new_id:
        if i.islower() == False and i != '-' and i != '_' and i != '.' and i.isnumeric() == False:
            return recom(new_id)
    
    if new_id[0] == '.' or new_id[-1] == '.' or '..' in new_id:
        return recom(new_id)
    
    return answer

'''
두번째 풀이
'''


def first(new_id):
    return new_id.lower()


def second(new_id):
    sc = ['-', '_', '.']
    str_temp = ''
    for char in new_id[:]:
        if char.islower() or char.isdigit() or char in sc:
            str_temp += char
    return str_temp


def third(new_id):
    while '..' in new_id:
        new_id = new_id.replace("..", ".")
    return new_id


def fourth(new_id):
    return new_id.strip('.')


def fifth(new_id):
    if not new_id:
        return 'a'
    else:
        return new_id


def sixth(new_id):
    if len(new_id) >= 16:
        return new_id[:15].strip('.')
    else:
        return new_id


def seventh(new_id):
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id


def solution(new_id):
    answer = ''
    new_id = first(new_id)
    new_id = second(new_id)
    new_id = third(new_id)
    new_id = fourth(new_id)
    new_id = fifth(new_id)
    new_id = sixth(new_id)
    new_id = seventh(new_id)
    answer = new_id
    return answer