import sys

N = int(sys.stdin.readline())  # 돌의 개수
stone = [0] + list(map(int, sys.stdin.readline().split()))

# stone 이진탐색
def binary_search(start, end):
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        
        visited = [False] * (N+1)
        flag = False
        
        stack = [1]
        visited[1] = True      # 1번 돌부터 시작하므로 True
        
        while stack:
            now = stack.pop()
            
            if now == N:
                flag = True
                break
            
            for idx in range(now+1, N+1):
                temp = (idx - now) * (1 + abs(stone[now] - stone[idx]))
                
                if temp <= mid and not visited[idx]:
                    stack.append(idx)
                    visited[idx] = True
                    
        if flag:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer

print(binary_search(1, (N-1) * (1 + abs(stone[N] - stone[1]))))