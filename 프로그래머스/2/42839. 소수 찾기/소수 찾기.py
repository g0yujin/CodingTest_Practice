from itertools import permutations
import math

def solution(numbers):
    
    permu = []
    # 순열 경우의 수 구하기
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            permu.append(j)

    # 튜플을 정수로 합치기
    num_list = []
    for i in permu:
        num = int(''.join(map(str, i)))
        num_list.append(num)

    # 중복 제거
    num_list = list(set(num_list))

    # 소수인지 확인하기
    answer = []
    for i in num_list:
        if i == 0 or i == 1:
            continue
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                break
        else:
            answer.append(i)

    return len(answer)

