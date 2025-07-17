import sys

N = int(sys.stdin.readline())
word = list(sys.stdin.readline().strip())
answer = 0

for i in range(N-1):
    compare = list(sys.stdin.readline().strip())
    temp = word.copy()


    for j in word:
        if j in compare:
            compare.remove(j)
            temp.remove(j)


    if len(temp) <= 1 and len(compare) <=1:
        answer += 1



print(answer)
