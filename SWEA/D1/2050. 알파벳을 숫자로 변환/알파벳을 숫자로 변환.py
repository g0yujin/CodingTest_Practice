import string

arr = input()
#대문자 리스트
upper = [i for i in string.ascii_uppercase]

result = []
for i in range(len(arr)):
    temp = upper.index(arr[i])
    result.append(temp+1)

print(*result)