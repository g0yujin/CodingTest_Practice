def solution(n):
    x = n**(1/2)
    
    if int(x) == x:
        return (x+1)**2
    else:
        return -1