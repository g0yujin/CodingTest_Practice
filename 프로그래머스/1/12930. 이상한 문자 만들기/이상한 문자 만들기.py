def solution(s):
    answer = ''
    
    idx = 0
    for i in s:
        if i == ' ':
            answer += ' '
            idx = 0
        elif idx % 2 == 0:
            answer += i.upper()
            idx += 1
        elif idx % 2 == 1:
            answer += i.lower()
            idx += 1
    return answer