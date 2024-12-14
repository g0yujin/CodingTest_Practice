def solution(num_list):
    hol = 0
    jjak = 0
    
    for i in range(1, len(num_list)+1):
        if i % 2 == 0:
            jjak += num_list[i-1]
        else:
            hol += num_list[i-1]
            
    return max(hol, jjak)