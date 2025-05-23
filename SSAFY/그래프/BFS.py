import sys

def bfs(start_node):
    # 큐에 들어가는 노드 = 다음에 방문해야 할 노드들(대기열)
    q = [start_node]  # 시작점을 넣은 상태로 출발
    # 1. 가장 앞에 있는 노드를 뽑는다
    # 2. 해당 노드에서 갈 수 있는 노드들을 큐에 넣는다.
    while q:
        now = q.pop(0)
        print(now, end=" ")

        for next_node in graph[now]:

            if visited[next_node]:  # 방문했으면 pass
                continue
            visited[next_node] = 1
            q.append(next_node)



N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s) # 양방향

visited[1] = 1
bfs(1)