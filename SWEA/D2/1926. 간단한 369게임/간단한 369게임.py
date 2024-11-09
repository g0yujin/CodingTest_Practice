N = int(input())

num = [i for i in range(1, N+1)]
answer = []
for i in range(N):      # 3,6,9가 있으면 그 수만큼 세서 -로
    count = 0
    if '3' in str(num[i]):
        count += str(num[i]).count('3')
    if '6' in str(num[i]):
        count += str(num[i]).count('6')
    if '9' in str(num[i]):
        count += str(num[i]).count('9')
    if count > 0:
        num[i] = '-'*count



print(*num)