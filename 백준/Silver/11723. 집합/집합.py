import sys

M = int(sys.stdin.readline())

S = set()
for _ in range(M):
    command = sys.stdin.readline().split()
    cal = command[0]
    num = 0
    if len(command) == 2:
        num = int(command[1])


    if cal== "add":
        if num not in S:
            S.add(num)

    elif cal == "remove":
        S.discard(num)

    elif cal == "check":
        if num in S:
            print(1)
        else:
            print(0)

    elif cal == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.add(num)

    elif cal == "all":
        S.update(range(1, 21))

    elif cal == "empty":
        S.clear()