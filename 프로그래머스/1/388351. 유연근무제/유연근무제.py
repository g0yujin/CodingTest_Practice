def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        time = schedules[i] + 10
        if time % 100 >= 60:
            time += 40
            
        count = 0
        
        for j in range(7):
            day = (startday + j) % 7
            
            if day == 6 or day == 0:
                 continue
                    
            present = timelogs[i][j]
            
            if present > time:
                count += 1
                
        if count == 0:
            answer += 1
            
    return answer
                
                
    
                
    
    
    
    
    
    
   