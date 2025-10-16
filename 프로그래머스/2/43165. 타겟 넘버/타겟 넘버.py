import itertools

def solution(numbers, target):
    n = len(numbers)
    sign = ['+', '-']
    sequences = list(itertools.product(sign, repeat=n))
    answer = 0
    
    for i in range(len(sequences)):
        current = sequences[i]
        total = 0
        for j in range(n):
            if current[j] == '+':
                total += numbers[j]
            else:
                total -= numbers[j]
                
        if total == target:
            answer += 1            
    
    return answer