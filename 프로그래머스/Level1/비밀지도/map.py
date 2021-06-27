def solution(n, arr1, arr2):
    answer = []
    arr_add  = []
    for a,b in zip(arr1, arr2):
        arr_add.append(a|b)
    
    for x in arr_add:
        x = str(bin(x))[2:]
        x= x.replace('1','#')
        x= x.replace('0',' ')
        if len(x)<n:
            x = (" " * (n- len(x))) + x
        answer.append(x)
    return answer
