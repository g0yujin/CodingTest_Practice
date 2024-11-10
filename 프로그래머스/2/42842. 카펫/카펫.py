def solution(brown, yellow):
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            y_h = i
            y_w = yellow // i
            
            count = (y_w + 2) * 2 + (y_h * 2)
            print(y_w, y_h)
            if count == brown:
                w = y_w + 2
                h = y_h + 2
                
                return [w, h]