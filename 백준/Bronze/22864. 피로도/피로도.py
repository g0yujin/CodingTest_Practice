import sys

A, B, C, M = map(int, sys.stdin.readline().split())
# A : 피로도 , B: 일처리, C: 회복도 M: 마지노선

fatigue = 0 # 초기 피로도
work = 0

for i in range(24):
    if fatigue > M:
        print(0)
    else:
        if fatigue + A <= M: # 일을 할 수 있는 경우
            work += B
            fatigue += A
        else:           # 일을 할 수 없는 경우
            if fatigue - C >= 0:
                fatigue -= C
            else:
                fatigue = 0

print(work)

