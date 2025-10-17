from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(i, j):
        
        queue = deque()
        queue.append((i, j))
        
        while queue:
            x, y = queue.popleft()
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    
        
    bfs(0, 0)


    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]

