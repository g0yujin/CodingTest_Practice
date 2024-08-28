a = int(input())
t = int(input())
x = int(input())

arr = []
bun = 1
degi = 1
n = 0

while True:
    prev_n = bun
    n += 1
    for _ in range(2):
        arr.append((bun, 0))
        bun += 1
        arr.append((degi, 1))
        degi += 1
    for _ in range(n+1):
        arr.append((bun, 0))
        bun += 1
    for _ in range(n+1):
        arr.append((degi, 1))
        degi += 1
    if prev_n < t <= bun:
        print(arr.index((t, x)) % a)
        break