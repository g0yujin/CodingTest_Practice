def solution(a, d, included):
    num_list = [i for i in range(a, a+ d*len(included), d)]
    answer = 0
    
    for i in range(len(included)):
        if included[i]:
            answer += num_list[i]
        else:
            pass
        
    return answer