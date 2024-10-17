def solution(clothes):

    # 딕셔너리로 만들기
    dict = {}
    for x, y in clothes:
        dict[x] = y
    
    
    # value의 개수 세기 - 종류별 의상의 개수 세기 
    count = {}
    for x, y in clothes:
        if y in count:
            count[y] += 1
        else:
            count[y] = 1
    
    answer = 1
    for value in count.values():
        answer *= (value + 1)
        
    return answer - 1