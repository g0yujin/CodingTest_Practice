def solution(num_list):
    gop = 1
    hap = 0
    
    for i in num_list:
        gop *= i
        hap += i
        
    hap = hap**2
    
    if gop < hap:
        return 1
    else:
        return 0