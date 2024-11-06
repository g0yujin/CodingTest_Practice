def solution(answers):
    su1 = [1,2,3,4,5] * 2000
    su2 = [2,1,2,3,2,4,2,5] * 1250
    su3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    cnt1, cnt2, cnt3 = 0, 0, 0
    
    for i in range(len(answers)):
        if su1[i] == answers[i]:
            cnt1 += 1
        if su2[i] == answers[i]:
            cnt2 += 1
        if su3[i] == answers[i]:
            cnt3 += 1
            
    result = max(cnt1, cnt2, cnt3)
    
    answer = []
    if cnt1 == result:
        answer.append(1)
    if cnt2 == result:
        answer.append(2)
    if cnt3 == result:
        answer.append(3)
        
    return answer
        