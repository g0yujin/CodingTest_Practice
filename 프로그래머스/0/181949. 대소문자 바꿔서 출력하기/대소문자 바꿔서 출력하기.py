str = input()
answer = ''
for i in str:
    if i.isupper():
        answer += i.lower()
    elif i.islower():
        answer += i.upper()

print(answer)
