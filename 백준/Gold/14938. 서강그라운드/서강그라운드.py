# n의 범위가 n (1 ≤ n ≤ 100)로 한정적 -> 플로이드 워셜

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())             # 지역 수, 수색 범위, 길의 개수
item = list(map(int, input().split()))
graph = [[INF] * (n+1) for i in range(n+1)]     # 2차원 리스트 만들고 무한으로 초기화

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 지역의 정보 입력받기
for i in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c


# 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


result = []      # 지역별 얻을 수 있는 최대 아이템의 개수
for a in range(1, n+1):
    temp = 0
    for b in range(1, n+1):
        if graph[a][b] <= m:
            temp += item[b-1]

    result.append(temp)

print(max(result))
