def solution(my_string, is_prefix):
    arr = []
    for i in range(len(my_string)+1):
        arr.append(my_string[:i+1])
        
    if is_prefix in arr:
        return 1
    else: return 0