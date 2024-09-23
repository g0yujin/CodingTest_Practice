import sys

N, M = map(int, sys.stdin.readline().split())
rank = {}     # 칭호
for i in range(N):
    name, score = sys.stdin.readline().split()
    rank[i] = int(score), name

# 이진탐색 함수
def binary_search(arr, target, start, end):
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if arr[mid][0] >= target:   # 범위에 맞는 경우
            end = mid - 1
            result = mid

        else:
             start = mid + 1

    return arr[result][1]

for j in range(M):
    target = int(sys.stdin.readline().rstrip())
    res = binary_search(rank, target, 0, N-1)
    print(res)
