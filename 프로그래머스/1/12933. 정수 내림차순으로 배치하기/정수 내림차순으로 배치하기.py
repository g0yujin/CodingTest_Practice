def solution(n):
    n = str(n)
    
    temp = []
    for i in n:
        temp.append(int(i))
    temp.sort(reverse=True)
    
    answer = ''
    for i in temp:
        answer+= str(i)
    return int(answer)