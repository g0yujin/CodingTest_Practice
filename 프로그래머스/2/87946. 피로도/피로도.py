from itertools import permutations

def solution(k, dungeons):
    # 최대 8 개밖에 안되니까 순열로
    arr = [i for i in range(len(dungeons))]
    num = []
    for i in permutations(arr, len(dungeons)):
        num.append(i)
        
        
    count = []    # 탐험할 수 있는 던전의 수 리스트 
    for i in num:
        temp = 0  # 각 경우의 수마다 탐험한 던전 수
        current_k = k
        for j in i:
            if current_k >= dungeons[j][0]:
                current_k -= dungeons[j][1]
                temp += 1
                
            else:
                continue
        count.append(temp)
        
        
    return max(count)