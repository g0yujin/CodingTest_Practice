def solution(genres, plays):
    
    # 장르별 재생횟수를 딕셔너리(dict)에 담기
    dict = {}
    for i in range(len(genres)):
        if genres[i] in dict:
            dict[genres[i]] += plays[i]
        else:
            dict[genres[i]] = plays[i]
    
    # 내림차순 정렬
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse = True)
    
    
    # 많이 재생된 장르 내에서 많이 재생된 노래
    answer = []
    for i in range(len(dict)):
        temp = {}
        for j in range(len(genres)):
            if genres[j] == sorted_dict[i][0]: 
                temp[j] =plays[j] 
                
        
        sorted_temp = sorted(temp.items(), key=lambda x: x[1], reverse = True)
        answer.append(sorted_temp[0][0])
        if len(sorted_temp) >= 2:
            answer.append(sorted_temp[1][0])
    
    return answer
    
    
    
    
    