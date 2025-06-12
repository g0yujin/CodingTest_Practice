import sys
N = int(sys.stdin.readline())

arr = []
for i in range(N):
    num = arr.append(int(sys.stdin.readline()))

arr.sort()
answer = []
for i in range(N):
    cnt = 5
    for j in range(arr[i], arr[i]+5):
        if j in arr:
            cnt -= 1

    answer.append(cnt)
print(min(answer))