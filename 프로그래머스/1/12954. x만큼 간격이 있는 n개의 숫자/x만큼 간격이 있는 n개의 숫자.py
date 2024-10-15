def solution(x, n):
    answer = []
    temp = 0
    while True:
        if len(answer) == n:
            break
        else:
            temp += x
            answer.append(temp)
            
    return answer