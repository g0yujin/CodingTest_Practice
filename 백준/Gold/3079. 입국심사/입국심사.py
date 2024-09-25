import sys

N, M = map(int, sys.stdin.readline().split())  # 입국심사대 수, 사람 수
time = []
for _ in range(N):
    time.append(int(sys.stdin.readline()))


start = min(time)
end = max(time) * M
result = float('inf')

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in time:
        total += mid // i

    if total >= M:
        end = mid - 1
        result = min(result, mid)

    else:
        start = mid + 1
print(result)