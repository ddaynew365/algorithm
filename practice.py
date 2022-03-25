def find(string):
    stack = []
    if not string or string[0] == '0':
        return []
    for i in range(len(string)):
        stack.append(string[i])
        if len(stack)/2 == len([x for x in stack if x == '1']):
            return stack
    return []
        
def largestMagical(binString):
    # Write your code here
    j = 0
    candidate = [binString]
    while j < len(binString):
        first = ''.join(find(binString[j:]))
        second = ''.join(find(binString[j+len(first):]))
        if first and second and first + second < second + first:
            remain_index =  len(first) + len(second) + j
            candidate.append(binString[:j]+ second + first + binString[remain_index:])
        j += 1
    return sorted(candidate)[-1]
  
print(largestMagical('10111000101100'))