def solution(a, b):
    answer = []
    answer.append(int(str(a) + str(b)))
    answer.append(2 * a* b)
    
    return max(answer)