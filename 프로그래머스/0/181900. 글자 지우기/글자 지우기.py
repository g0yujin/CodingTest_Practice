def solution(my_string, indices):
    index_set = set(indices)
    result = []
    
    # 문자열의 각 문자에 대해 반복
    for i, char in enumerate(my_string):
        # 인덱스가 제거할 인덱스 집합에 없으면 해당 문자를 결과에 추가
        if i not in index_set:
            result.append(char)
    
    # 리스트를 다시 문자열로 결합하여 반환
    return ''.join(result)