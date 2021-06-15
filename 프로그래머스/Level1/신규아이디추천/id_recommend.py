
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
