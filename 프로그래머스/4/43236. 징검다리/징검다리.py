def solution(distance, rocks, n):
    answer = 0
    
    rocks.append(distance)
    rocks.sort()     # 이분탐색을 위해 정렬
    
    start = 1
    end = distance
    
    while start <= end:
        mid = (start + end) // 2
        
        previous = 0   # 현재 위치
        count = 0
        
        for rock in rocks:
            if rock - previous < mid:
                count += 1
                if count > n:
                    break
            else:
                previous = rock
                    
        if count > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
            
    return answer
        
        