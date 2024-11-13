T = int(input())

for i in range(1, T+1):
    arr = input()
    if arr == arr[::-1]:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')