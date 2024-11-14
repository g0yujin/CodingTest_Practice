def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        temp = [i+j for i, j in zip(arr1[i], arr2[i])]
        result.append(temp)
    
    return result