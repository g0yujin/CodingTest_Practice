import sys

N = int(sys.stdin.readline())

cookie = []
for i in range(N):
    cookie.append(list(sys.stdin.readline().strip()))

la, ra, w, ll, rl = 0, 0, 0, 0, 0
heart = []

# 심장 위치 찾기
for i in range(N):
    for j in range(N):
        if cookie[i][j] == '*':
            heart.append(i+2)
            heart.append(j+1)
            break
    if heart:
        break

#왼팔, 오른팔 길이
for i in range(N):

    if i < heart[1]-1 and cookie[heart[0]-1][i] == '*':   # 왼팔
        la += 1
    if i > heart[1]-1 and cookie[heart[0]-1][i] == '*':  # 오른팔
        ra += 1

    if i > heart[0]-1 and cookie[i][heart[1]-1] == '*': # 허리
        w += 1

    if i > heart[0]-1+w and cookie[i][heart[1]-2] == '*':
        ll += 1

    if i > heart[0] - 1 + w and cookie[i][heart[1]] == '*':
        rl += 1



print(heart[0], heart[1])
print(la, ra, w, ll, rl)