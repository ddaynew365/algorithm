import sys
M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    command = list(sys.stdin.readline().split())
    if command == ["all"]:
        S = set([x for x in range(1, 21)])
        continue
    elif command == ["empty"]:
        S = set()
        continue

    command, num = command[0], int(command[1])

    if command == "add":
        S.add(num)
    elif command == "remove":
        S.discard(num)
    elif command == "check":
        if num in S:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if num in S:
            S.discard(num)
        else:
            S.add(num)
