def solution(s):
    answer = 0
    alpha = {
        'zero': '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9',
    }

    for key in alpha:
        s = s.replace(key, alpha[key])
    return int(s)