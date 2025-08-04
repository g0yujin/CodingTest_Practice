import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
max_num = 100000
visited = [0] * (max_num + 1)

def bfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()

        if x == K:
            print(visited[x])
            break

        for j in (x-1, x+1, x*2):
            if 0 <= j <= max_num and not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)
bfs()
