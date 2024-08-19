import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited_dfs = [False] * (N + 1)  # dfs의 방문기록
visited_bfs = [False] * (N + 1)  # bfs의 방문기록


def bfs(V):
    q = deque([V])
    visited_bfs[V] = True  # 해당 V 값을 방문처리
    while q:  # q가 빌때까지 돈다.
        V = q.popleft()  # 큐에 있는 첫번째 값 꺼낸다.
        print(V, end=" ")  # 해당 값 출력
        for i in range(1, N + 1):  # 1부터 N까지 돈다
            if not visited_bfs[i] and graph[V][i]:  # 만약 해당 i값을 방문하지 않았고 V와 연결이 되어 있다면
                q.append(i)  # 그 i 값을 추가
                visited_bfs[i] = True  # 방문처리


def dfs(V):
    visited_dfs[V] = True  # 방문 처리
    print(V, end=" ")
    for i in range(1, N + 1):
        if not visited_dfs[i] and graph[V][i]:  # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i)  # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)


dfs(V)
print()
bfs(V)
