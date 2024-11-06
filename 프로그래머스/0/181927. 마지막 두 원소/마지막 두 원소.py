def solution(num_list):
    num1 = num_list[-1]
    num2 = num_list[-2]
    
    if num1 > num2 :  # 마지막 원소가 더 클 때
        num_list.append(num1 - num2)
    else:    # 그 전 원소가 클 때
        num_list.append(num1*2)
        
    return num_list