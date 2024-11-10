def solution(left, right):
    num = [i for i in range(left, right+1)]
    answer = 0
    
    for i in num:
        count = 0     # 약수의 개수
        for j in range(1, i+1):
            if i % j == 0:
                count += 1    
                
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    
        
    return answer