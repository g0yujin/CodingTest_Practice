def solution(t, p):
    arr = []
    
    for i in range(len(t)-len(p)+1):
        arr.append(int(t[i:i+len(p)]))
    
    cnt = 0
    for i in arr:
        if i <= int(p):
            cnt += 1
            
    return cnt