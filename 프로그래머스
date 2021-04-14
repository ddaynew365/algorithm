def solution(numbers):
    strs = []
    dict_ = {}
    answer = ''

    for i in numbers:
        values = i

        if i == 0:
            continue

        else:
            if i / 10 >= 1:
                i = i / 10

            else:
                dict_[i] = values

            while i >= 1:

                if i / 10 >= 1:
                    i = i / 10

                else:
                    dict_[i] = values
                    break
    print(dict_)
    key_num = list(dict_.keys())
    print(key_num)
    key_num = sorted(key_num)
    print(key_num)
    key_num.reverse()

    for i in key_num:
        strs.append(str(dict_[i]))

    for i in strs:
        answer = answer + i

    return answer

number = [6, 10, 2]
print(solution(number))
