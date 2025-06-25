import sys

word = sys.stdin.readline().upper().strip()

dict = {}
for i in word:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

max_value = []

for key, value in dict.items():
    if max(dict.values()) == value:
        max_value.append(key)

if len(max_value) == 1:
    print(*max_value)
else:
    print('?')