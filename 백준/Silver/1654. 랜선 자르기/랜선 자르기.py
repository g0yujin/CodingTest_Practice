import sys

K, N = map(int, sys.stdin.readline().split()) # 보유 랜선 개수, 필요 랜선 개수
lan = []
for i in range(K):
    lan.append(int(sys.stdin.readline()))


start = 1
end = max(lan)
length = []        # 랜선의 최대 길이

while start <= end:
    num = 0       # 랜선 개수
    mid = (start + end) // 2

    for i in lan:
        num += i // mid

    if num < N:

        end = mid - 1

    else:
        length.append(mid)
        start = mid + 1

print(max(length))