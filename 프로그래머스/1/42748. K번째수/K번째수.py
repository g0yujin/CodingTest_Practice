def solution(array, commands):
    answer = []
    
    for i in commands:
        i, j, k = i[0], i[1], i[2]
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
        
    return answer