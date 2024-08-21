import sys
from collections import deque

#    상  하  좌  우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# BFS - 이미 지나온 곳은 0으로 바꾸기
def bfs(house, a, b):
    queue = deque()
    queue.append((a, b))
    house[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue
            if house[next_x][next_y] == 1:
                house[next_x][next_y] = 0
                queue.append((next_x, next_y))
                count += 1

    return count


N = int(sys.stdin.readline())

house = []
complex = []

for i in range(N):
    house.append(list(map(int, sys.stdin.readline().rstrip())))


for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            complex.append(bfs(house, i, j))


complex.sort()
print(len(complex))
for i in range(len(complex)):
    print(complex[i])