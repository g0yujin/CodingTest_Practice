import sys
N = int(sys.stdin.readline()) # 집 수
arr = list(map(int, sys.stdin.readline().split())) # 난로의 반지름 길이
answer = 0  # 연탄 사용이 가능한 최대 집의 수

for i in range(2, max(arr)+1):
    temp = 0
    for j in range(N):
        if arr[j] % i == 0:
            temp += 1

    answer = max(temp, answer)

print(answer)