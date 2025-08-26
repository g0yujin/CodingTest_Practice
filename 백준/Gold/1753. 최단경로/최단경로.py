import sys, heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

graph = [ [] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))

def dijkstra(graph, start):

    distance = [float('inf')] * (V+1)
    distance[start] = 0

    heap = [[0, start]]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        # 이미 처리됐으면 건너뛰기
        if current_dist > distance[current_node]:
            continue


        for next_node, weight in graph[current_node]:
            new_dist = current_dist + weight

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    return distance

distances = dijkstra(graph, K)

for i in range(1, V+1):
    if distances[i] == float('inf'):
        print('INF')
    else:
        print(distances[i])