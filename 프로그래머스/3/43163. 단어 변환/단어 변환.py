from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    
    return bfs(begin, target, words)
        
        
def bfs(begin, target, words):
    
    queue = deque()
    queue.append((begin, 0))
    visited = set([begin])
    
    while queue:
        now, step = queue.popleft()
        
        if now == target:
            return step
            
        for word in words:
            if word in visited:
                continue
                
            count = 0
            for i in range(len(begin)):
                if now[i] != word[i]:
                    count += 1
                    
            if count == 1:
                queue.append((word, step+1))
                visited.add(word)
                
    return 0
    
    
        
    