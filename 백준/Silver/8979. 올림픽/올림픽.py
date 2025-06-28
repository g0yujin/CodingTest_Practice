import sys

N, K = map(int, sys.stdin.readline().split())

contry = []
want = 0
for i in range(N):
    contry.append(list(map(int, sys.stdin.readline().split())))
    if contry[i][0] == K:
        want = i

answer = 1

for i in range(N):
    if i == want: continue # 본인제외

    # 1. 금메달 비교
    if contry[i][1] > contry[want][1]: # 금메달 개수가 많을 때
        answer += 1

    # 2. 금메달 개수가 같다 = 은메달 비교
    elif contry[i][1] == contry[want][1]:
        if contry[i][2] > contry[want][2]:
            answer += 1

        elif contry[i][2] == contry[want][2]: # 은메달 수까지 같을 때
            if contry[i][3] > contry[want][3]:
                answer += 1
            else:
                continue


print(answer)