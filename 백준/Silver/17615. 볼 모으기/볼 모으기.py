import sys

N = int(sys.stdin.readline())
ball = list(sys.stdin.readline().strip())

# 색 별로 구분
red = [0] * N
blue = [0] * N
red_count = 0
blue_count = 0

for i in range(N):
    if ball[i] == 'R':
        red[i] = 1
        red_count += 1
    else:
        blue[i] = 1
        blue_count += 1



answer = sys.maxsize

# 왼쪽에 몰기 - red
for i in range(N):
    if red[i] == 0:
        start_idx = i
        break
count = red_count - start_idx
answer = min(answer, count)
# 왼쪽에 몰기 - blue
for i in range(N):
    if blue[i] == 0:
        start_idx = i
        break
count = blue_count - start_idx
answer = min(answer, count)
# 오른쪽에 몰기 - red
for i in range(N-1, -1, -1):
    if red[i] == 0:
        start_idx = i
        break
count = red_count - (N-1-start_idx)
answer = min(answer, count)
# 오른쪽에 몰기 - blue
for i in range(N-1, -1, -1):
    if blue[i] == 0:
        start_idx = i
        break
count = blue_count - (N-1-start_idx)
answer = min(answer, count)

print(answer)