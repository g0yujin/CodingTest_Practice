import sys
input = sys.stdin.readline
INF = 987654321
n = int(input())

graph = [[INF]*59 for _ in range(59)]  # ord를 이용할 것이라 59개로 만들어줌

for _ in range(n):
    x, y = input().rstrip().split(" => ")
    graph[ord(x)-64][ord(y)-64] = 0  # 단방향 그래프

def floyd():
    for i in range(59):
        for j in range(59):
            for k in range(59):
                if j == k: continue
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

floyd()
res = []  # 명제를 저장할 리스트
cnt = 0  # 개수를 세어줄 변수

for i in range(59):
    for j in range(59):
        if i != j and graph[i][j] == 0:  # i와 j가 같은 경우를 제외해주어야 한다.
            res.append(f'{chr(i+64)} => {chr(j+64)}')
            cnt += 1

print(cnt)
for i in res:
    print(i)