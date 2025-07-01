import sys

N, kind = sys.stdin.readline().split()

request = []
for i in range(int(N)):
    request.append(sys.stdin.readline().strip())

# 이미 한 사람들은 리스트에서 지우기
request = set(request)
answer = 0

if kind == 'Y':
    print(len(request))

elif kind == 'F':
    print(len(request) // 2)

elif kind == 'O':
    print(len(request) // 3)


