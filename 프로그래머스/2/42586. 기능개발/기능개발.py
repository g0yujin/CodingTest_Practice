import math

def solution(progresses, speeds):
    day_list = []
    for i in range(len(progresses)):
        day_list.append(math.ceil((100 - progresses[i])/ speeds[i]))
        
    answer_list = []
    i = 0
    answer = 1
    day = day_list[i]
    
    while True:
        if day_list[i+1] <= day:
            answer += 1
            i += 1
        else:
            day = day_list[i+1]
            answer_list.append(answer)
            answer = 0
        if i+1 == len(day_list):
            answer_list.append(answer)
            break
            
            
    return answer_list