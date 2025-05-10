def solution(n, w, num):
    
    
    h = 0    # 층 수
    result = 0
    
    if n % w == 0:   
        h = n//w 
        
    else:
        h = n // w + 1
    
    arr = [[0 for _ in range(w)] for _ in range(h)]
    
    # 택배 놓기
    box = 1
    num_i = 0
    num_j = 0
    
    for i in range(h):
        if box == n+1:
            break
        # 짝수행
        if i % 2 == 0:
            for j in range(w):
                if box == num:
                    num_i = i
                    num_j = j
                
                if box <= n:
                    arr[i][j] = box
                    box += 1
            
        # 홀수행
        else:
            for j in range(w-1, -1, -1):
                if box == num:
                    num_i = i
                    num_j = j
                    
                if box <= n:
                    arr[i][j] = box
                    box += 1
    
    
    for i in range(num_i, h):
        if arr[i][num_j] != 0:
            result += 1
    
    return result