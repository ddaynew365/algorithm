def solution(name):
    answer, idx = 0, 0
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]

    while True:
        answer += change[idx]
        change[idx] = 0
        if sum(change) == 0:
            return answer

        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1

        if left < right:
            answer += left
            idx += -left
        else:
            answer += right
            idx += right
    return answer