def solution(a, b, c):
    answer = 0
    if a != b and b != c and a != c: # 세 숫자가 모두 다를 때
        answer = a + b + c
    elif (a == b and b != c) or (a == c and a != b) or (b == c and c != a):
        answer = (a + b + c) * (a**2 + b**2 + c**2)
        
    else:
        answer = (a + b + c) * (a**2 + b**2 + c**2 ) * (a**3 + b**3 + c**3)
                                                         
    return answer