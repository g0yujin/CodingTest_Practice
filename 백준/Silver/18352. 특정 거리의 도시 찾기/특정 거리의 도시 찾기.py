import sys
from collections import deque

# 도시수, 도로 개수, 거리 정보, 출발 도시
n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (n+1)
distance[x] = 0   # 출발 도시 -> 출발 도시로 가는 최단 거리는 항상 0

queue = deque([x])
while queue:
    now = queue.popleft()
    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            queue.append(i)

if k in distance:
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)
else:
    print(-1)