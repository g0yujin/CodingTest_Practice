import sys

n = int(sys.stdin.readline())

if n == 1:
    print('*')

else:
    for i in range(1, n):
        last = (n - i) * 4 + 1
        print("* " * (i - 1) + "*" * last + " *" * (i - 1))
        print("* " * i + " " * (last - 4) + " *" * i)
    print("* " * (2 * n - 1))
    for i in range(n - 1, 0, -1):
        last = (n - i) * 4 + 1
        print("* " * i + " " * (last - 4) + " *" * i)
        print("* " * (i - 1) + "*" * last + " *" * (i - 1))

