def solution(s):
    idx = len(s) // 2
    
    if len(s) % 2 == 0:  # 짝수일 때
        return s[idx-1:idx+1]
    else:
        return s[idx]
        
    