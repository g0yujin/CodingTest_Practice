import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 100만으로 늘림

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]   # 연결 정보를 저장할 linked list 배열

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


# 부모 - 자식 관계 알아내기 - DFS
parent = [0] * (N+1)

def dfs(v):
    for i in graph[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(i)

dfs(1)

for j in range(2, N+1):
    print(parent[j])