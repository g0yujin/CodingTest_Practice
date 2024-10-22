def solution(s):
    count = 0

    # 괄호 순서와 개수를 확인
    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        
        # 오른쪽 괄호가 더 많아지면 잘못된 괄호 문자열
        if count < 0:
            return False

    # 최종적으로 괄호의 짝이 맞아야 하므로 count는 0이어야 함
    return count == 0
