import sys

N = int(sys.stdin.readline())
result = 0

for i in range(1, N+1): # 1부터 N까지
    split = list(map(int, str(i)))  # 숫자 분해
    result = sum(split) + i         # 분해합

    if result == N:
        print(i)
        break        # 제일 작은 숫자만 출력해야되니까 반복문 나가기
    elif i == N:
        print(0)

