import string

# 대문자 리스트
upper = [i for i in string.ascii_uppercase]

arr = input()
answer = []
for i in range(len(arr)):
    for j in upper:
        if arr[i] == j:
            answer.append(upper.index(j)+1)



print(*answer)