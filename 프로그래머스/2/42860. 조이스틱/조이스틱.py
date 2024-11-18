def solution(name):
    n = len(name)
    min_move = n - 1
    answer = 0
    
    for i, char in enumerate(name):
        # 상하 이동
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 좌우 이동
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1
            
        min_move = min([min_move, 
                       2 * i + n - next,  # 왼쪽으로 갔다가 오른쪽
                       i + 2 * (n - next)])  # 오른쪽으로 갔다가 왼쪽
            
    return answer + min_move