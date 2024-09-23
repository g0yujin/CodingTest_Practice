import sys

N, M = map(int, sys.stdin.readline().split())
dots = list(map(int, sys.stdin.readline().split()))
dots.sort()

def dot_min(a):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        if a > dots[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return end + 1

def dot_max(b):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        if b >= dots[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return end

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(dot_max(b) - dot_min(a) + 1)