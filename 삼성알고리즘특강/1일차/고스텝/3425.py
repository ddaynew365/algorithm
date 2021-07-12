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
    if a == 0:
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
    if a == 0:
        error = True
        return stack, error
    if a < 0:
        a = abs(a)
        sig += 1
    b_flag = True
    if b < 0:
        b = abs(b)
        sig += 1
        b_flag = False

    if sig % 2 == 0:
        if b_flag == True:
            stack.append(b % a)
        else:
            stack.append(-(b % a))
    else:
        stack.append(-(b % a))

    return stack, error




quit = False
while True: # 프로그램
    cmds= []
    while True: # 명령어 받기
        user = sys.stdin.readline().strip()
        cmds.append(user)
        if user == 'QUIT':
            quit = True
            break
        if user == 'END':
            print()
            break
    if quit == True:
        break
    N = int(sys.stdin.readline().strip())

    for _ in range(N):
        num = int(sys.stdin.readline().strip())
        stack = [num]
        for cmd in cmds:
            error = False
            if cmd.startswith("NUM"):
                stack = num_x(stack, cmd)
            elif cmd == "POP":
                stack,error = pop(stack,error)
            elif cmd == "INV":
                stack,error = inv(stack,error)
            elif cmd == "DUP":
                stack,error = dup(stack,error)
            elif cmd == "SWP":
                stack,error = swp(stack,error)
            elif cmd == "ADD":
                stack, error = add(stack, error)
            elif cmd == "SUB":
                stack, error = sub(stack, error)
            elif cmd == "MUL":
                stack, error = mul(stack, error)
            elif cmd == "DIV":
                stack, error = div(stack, error)
            elif cmd == "MOD":
                stack, error = mod(stack, error)
            elif cmd == "END":
                if len(stack) == 1:
                    print(stack[0])
                else:
                    print("ERROR")
            else:
                break

            if error == True:
                print("ERROR")
                break
