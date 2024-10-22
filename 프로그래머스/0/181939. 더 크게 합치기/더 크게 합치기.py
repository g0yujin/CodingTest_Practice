def solution(a, b):
    answer = []
    answer.append(int(str(a)+str(b)))
    answer.append(int(str(b)+str(a)))
    return max(answer)