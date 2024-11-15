def solution(n, lost, reserve):
    # 여분이 있는 학생이 잃어버렸을 때 -> 교집합
    intersection = list(set(lost) & set(reserve))
    
    for i in intersection:
        reserve.remove(i)
        lost.remove(i)
    lost.sort()
    temp = lost.copy()
    for i in temp: 
        if i-1 in reserve:
            reserve.remove(i-1)
            lost.remove(i)
                
        elif i+1 in reserve:
            reserve.remove(i+1)
            lost.remove(i)
        
            
    return n-len(lost)
        
        