import sys
import heapq

# 노드의 개수가 최대 20000개 이므로 우선순위큐를 이용한 다익스트라 알고리즘 사용

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
start = int(input())
graph = [[] for i in range(V+1)]  # 각 노드에 연결되어 있는 노드에 대한 정보
distance = [INF] * (V+1)          # 최단 거리 테이블

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 다익스트라 알고리즘
def dijkstar(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:    # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)    # 큐에서 최단거리가 가장 짧은 노드 정보 꺼내기
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstar(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])