import sys
big_num = 1000000000

def num_x(stack, cmd):
    cmd, x = cmd.split()
    x = int(x)
    stack.append(x)
    return stack

def pop(stack, error):
    if len(stack) < 1:
        error = True
        return stack, error
    stack.pop()
    return stack, error

def inv(stack, error):
    if len(stack) < 1:
        error = True
        return stack, error
    stack[-1] = -stack[-1]
    return stack, error

def dup(stack, error):
    if len(stack) < 1:
        error = True
        return stack, error
    stack.append(stack[-1])
    return stack, error

def swp(stack, error):
    if len(stack) < 2:
        error = True
        return stack, error
    stack[-1], stack[-2] = stack[-2],stack[-1]
    return stack, error

def add(stack, error):
    if len(stack) < 2:
        error = True
        return stack, error
    a = stack.pop()
    b = stack.pop()
    if b+a > abs(big_num):
        error = True
        return stack, error
    stack.append(b+a)
    return stack, error

def sub(stack, error):
    if len(stack) < 2:
        error = True
        return stack, error
    a = stack.pop()
    b = stack.pop()
    if b+a > abs(big_num):
        error = True
        return stack, error
    stack.append(b - a)
    return stack, error

def mul(stack, error):
    sig = 0
    if len(stack) < 2:
        error = True
        return stack, error
    b = stack.pop()
    a = stack.pop()
    if a*b > abs(big_num):
        error = True
        return stack, error

    stack.append(b*a)

    return stack, error

def div(stack, error):
    sig = 0
    if len(stack) < 2:
        error = True
    a = stack.pop()
    b = stack.pop()
    if b == 0:
        error = True
        return stack, error
    if a < 0:
        a = abs(a)
        sig += 1
    if b < 0:
        b = abs(b)
        sig += 1

    if sig % 2 == 0:
        stack.append(b // a)
    else:
        stack.append(-(b // a))

    return stack, error

def mod(stack, error):
    sig = 0
    if len(stack) < 2:
        error = True
    a = stack.pop()
    b = stack.pop()
    if b == 0:
        error = True
        return stack, error
    if a < 0:
        a = abs(a)
        sig += 1
    if b < 0:
        b = abs(b)
        sig += 1

    if sig % 2 == 0:
        stack.append(b % a)
    else:
        stack.append(-(b % a))

    return stack, error

N = int(input())

stack = []
while True:
    error = False
    cmd = sys.stdin.readline().strip()
    if cmd.startswith("NUM"):
        stack, flag = num_x(stack, flag)
    elif cmd == "POP":
        stack = pop(stack)
    elif cmd == "INV":
        stack = inv(stack)
    elif cmd == "DUP":
        stack = dup(stack)
    elif cmd == "SWP":
        stack = swp(stack)
    elif cmd == "ADD":
        stack, flag = (stack, flag)
    elif cmd == "SUB":
        stack, flag = sub(stack, flag)
    elif cmd == "MUL":
        stack, flag = mul(stack, flag)
    elif cmd == "DIV":
        stack, flag = div(stack, flag)
    elif cmd == "MOD":
        stack, flag = mod(stack, flag)
    else:
        break

    if error == True:
        break
