import sys

N, T, P = map(int, sys.stdin.readline().split())
score = []
if N > 0:
    score = list(map(int, sys.stdin.readline().split()))

# N이 0인 경우 (랭킹 리스트가 비어있는 경우)
if N == 0:
    print(1)
else:
    # 랭킹 리스트가 꽉 차있고, 새로운 점수가 마지막 점수보다 작거나 같은 경우
    if N == P and T <= score[-1]:
        print(-1)
    else:
        # 새로운 점수보다 큰 점수의 개수를 세어서 등수 계산
        rank = 1
        for s in score:
            if s > T:
                rank += 1
            else:
                break
        print(rank)