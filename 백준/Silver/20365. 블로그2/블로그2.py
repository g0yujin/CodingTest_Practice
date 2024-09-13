import sys

N = int(sys.stdin.readline())
color = sys.stdin.readline()

cnt_B = color.count("B")
cnt_R = color.count("R")

result_R = 1
result_B = 1

# 파란색을 먼저 칠해야될 떄
for i in range(N):
    if color[i] == "R" and color[i+1] == "B":
        result_R += 1
    if color[i] == "R" and i == N-1:
        result_R += 1



for i in range(N):
    if color[i] == "B" and color[i+1] == "R":
        result_B += 1
    if color[i] == "B" and i == N-1:
        result_B += 1



print(min(result_B, result_R))
