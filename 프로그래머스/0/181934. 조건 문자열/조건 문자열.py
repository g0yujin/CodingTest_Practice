def solution(ineq, eq, n, m):
    answer = ''
    
    if eq == '=':
        if ineq == ">":
            answer = n >= m
        else:
            answer = n <= m
    else:
        if ineq == "<":
            answer = n < m
        else:
            answer = n > m 
    
    if answer:
        return 1
    else: 
        return 0