def solution(numbers):
    num = [i for i in range(0, 10)]

    for i in numbers:
        if i in num:
            num.remove(i)
    
    return sum(num)