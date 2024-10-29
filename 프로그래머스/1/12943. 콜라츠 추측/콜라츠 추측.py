def solution(num):
    
    count = 0    # 작업 횟수
    
    while True:
        if count >= 500:
            return -1
        if num == 1:
            return count
        
        if num % 2 == 0 and count < 500:
            num //= 2
            count += 1
            
        elif num % 2 != 0 and count < 500:
            num = num * 3 + 1
            count += 1
            