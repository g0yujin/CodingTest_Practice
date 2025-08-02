import sys
# N:접시 수 / D:초밥종류 수 / K: 연속해서 먹는 접시 수/ C: 쿠폰 번호
N, D, K, C = map(int, sys.stdin.readline().split())

sushi = []
for i in range(N):
    sushi.append(int(sys.stdin.readline()))

sushi = sushi + sushi[:K-1]
count = 0
for i in range(N):
    temp = sushi[i:i+K]
    # K개 안에 쿠폰 번호가 있다 = 개수 그대로
    if C in temp:
        count = max(count, len(set(temp)))
    # K개 안에 쿠폰 번호가 없다 = 개수 +1
    else:
        count = max(count, len(set(temp))+1)

print(count)