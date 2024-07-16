import sys

T = int(sys.stdin.readline())


for i in range(T):
    R, S = sys.stdin.readline().split()
    result = []

    for j in S:
        result.append(j*int(R))

    print(''.join(result))



