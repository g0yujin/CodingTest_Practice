import sys
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]



def dfs(x, y):
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
            dfs(nx, ny)


# 0.  입력 및 초기화
T = int(sys.stdin.readline())

for _ in range(T):
    # 가로, 세로, 배추 위치 개수
    M, N, K = map(int, sys.stdin.readline().split())

    graph = [[0] * M for _ in range(N)]

    #1. 그래프 정보 입력
    for i in range(K):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1

    # 2. dfs 함수 작성
    answer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(i, j)
                answer += 1


    print(answer)

