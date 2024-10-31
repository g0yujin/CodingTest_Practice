def solution(code):
    result = ''
    mode = 0
    
    for i in range(len(code)):
        if mode == 0:          # 모드가 0일 때
            if code[i] == '1':   # 모드바꾸기
                mode = 1
            elif i % 2 == 0 :     # idx가 짝수일 때
                result += code[i]
                
        else:                  # 모드가 1일 때
            if code[i] == '1':
                mode = 0
            elif i % 2 == 1:    # idx가 홀수일 때
                result += code[i]
                
    if len(result) == 0:
        return "EMPTY"
    else:
        return result
                