from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1] * 102 for i in range(102)]
    
    
    for r in rectangle:
        
        # 모든 좌표값 2배
        x1, y1, x2, y2 = map(lambda x: x*2 , r)
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # 직사각형 내부는 0
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1
                    
                    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((characterX*2, characterY*2))
    visited = [[0] * 102 for i in range(102)]
    
    while queue:
        x, y = queue.popleft()
        
        if x == itemX*2 and y == itemY*2:
            return visited[x][y] // 2
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    
                 
                    