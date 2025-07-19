import sys

T = int(sys.stdin.readline())

for test_case in range(T):
    # N: 팀의 개수, K: 문제의 개수, T: 우리팀ID, M: 로그엔트리 개수
    N, K, T, M = map(int, sys.stdin.readline().strip().split())

    submit = [0] * (N + 1)  # 제출 횟수
    score = [[0] * (K + 1) for _ in range(N + 1)]  # 문제별 점수
    last_submit = [0] * (N+1) # 마지막 제출 시간

    for i in range(M):
        # t: 팀ID, p: 문제번호, s:획득점수
        t, p, s = map(int, sys.stdin.readline().split())
        submit[t] += 1
        last_submit[t] = i
        if s > score[t][p]:
            score[t][p] = s

    # 총 점수 구하기
    total = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            total[i] += score[i][j]

    # 우리 팀의 순위 구하기
    rank = 1
    for i in range(1, N+1):
        if i == T:
            continue
        elif total[i] > total[T]: # 우리 팀보다 점수가 높은 경우
            rank += 1

        elif total[i] == total[T]:  # 우리 팀이랑 점수가 같은 경우
            # 1. 제출 횟수가 적으면 이김
            if submit[i] < submit[T]:
                rank += 1
            elif submit[i] == submit[T]:   # 제출 횟수도 같을 때 = 제출 시간이 빠른 경우 이김
                if last_submit[i] < last_submit[T]:
                    rank += 1

    print(rank)