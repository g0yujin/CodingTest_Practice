from collections import deque

def solution(n, computers):
    
    visited = [False] * n
    answer = 0
    
    def bfs(v):
        queue = deque()
        queue.append(v)
        
        while queue:
            current = queue.pop()
            
            for i in range(n):
                if computers[current][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
            
    return answer
        
               