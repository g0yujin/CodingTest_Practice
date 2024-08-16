import sys

# 파일 수
N = int(sys.stdin.readline())
extension = {}

for i in range(N):
    file = sys.stdin.readline().rstrip()
    for j in range(len(file)):
        if file[j] == '.':
            word = file[j+1:len(file)]
            if word not in extension:
                extension.update({word: 1})
            elif word in extension:
                extension[word] += 1

for key, value in sorted(extension.items()):
    print(key, value)
