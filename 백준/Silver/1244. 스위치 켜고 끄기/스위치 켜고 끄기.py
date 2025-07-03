import sys

N = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline())
for i in range(S):
    gender, num = map(int, sys.stdin.readline().split())

    if gender == 1: # 남학생일 때
        for j in range(num-1, N, num):
            if switch[j] == 1:
                switch[j] = 0
            else: switch[j] = 1

    else: # 여학생일 때
        left = num-2
        right = num
        while True:
            if left >= 0 and right <=(N-1) and switch[left] == switch[right]:

                left -= 1
                right += 1
            else:
                break


        for j in range(left+1, right):
            if switch[j] == 1:
                switch[j] = 0

            else:
                switch[j] = 1


if len(switch) > 20:
    for j in range(0, len(switch), 20):
        print(*switch[j:j+20])

else:
    print(*switch)

