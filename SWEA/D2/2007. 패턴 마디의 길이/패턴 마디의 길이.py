T = int(input())

for i in range(T):
    arr = input()
    for j in range(len(arr)):
        temp = arr[:j+1]
        if temp == arr[j+1:j+len(temp)+1]:
            print(f'#{i+1} {len(temp)}')
            break


