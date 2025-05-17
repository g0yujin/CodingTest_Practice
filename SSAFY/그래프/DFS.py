'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''

import sys

# DFS 구현
def dfs(node):
    # 종료조건 - ex) K개의 노드를 방문했다면, N개를 모두 방문했다면 경로 출력

    print(node, end=" ")
    visited[node] = 1  # 시작점 방문 처리

    for next_node in graph[node]: # 현재 노드에서 인접한 노드들을 모두 확인하면서 한 군데로 진행
        if visited[next_node]:  # 이미 방문했다면 가지 마라
             continue

        visited[next_node] = 1   # 방문하지 않았다면 -> 방문 처리
        dfs(next_node)


N, M = map(int, sys.stdin.readline().split())
# 1. 그래프 저장하기 - 비어있는 그래프 생성 후 정보 넣기 (인접 행렬 or 인접 리스트)
# graph = [[0] * (N+1) for _ in range(N+1)] -> 인접행렬
graph = [[] for _ in range(N+1)] #-> 인접 리스트

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

# 방문 여부 기록
visited = [0] * (N+1)
dfs(1)