import sys

N, M = map(int, sys.stdin.readline().split()) # 나무의 수, 가져가려는 나무 길이
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)   # 나무 높이의 최댓값을 end로 설정
height = 0         # 절단기 높이

while start <= end:
    result = 0
    mid = (start + end) // 2

    for i in trees:
        if i > mid:
            result += i - mid

    if result >= M:
        height = mid
        start = mid + 1

    else:
        end = mid - 1


print(height)
