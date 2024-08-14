import sys

n = int(sys.stdin.readline())
mine = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
player = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
answer = [['.'] * n for i in range(n)]  # 초기화

# 8 방향 탐색을 위한 벡터
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 지뢰를 클릭했는지 여부
mine_clicked = False

# 주변 지뢰 수 계산
for x in range(n):
    for y in range(n):
        if player[x][y] == 'x':
            if mine[x][y] == '*':
                mine_clicked = True  # 지뢰를 클릭한 경우
            else:
                # 주변 지뢰 수 계산
                count = 0
                for j in range(8):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if 0 <= nx < n and 0 <= ny < n and mine[nx][ny] == '*':
                        count += 1
                answer[x][y] = str(count)

# 지뢰를 클릭한 경우 모든 지뢰 표시
if mine_clicked:
    for x in range(n):
        for y in range(n):
            if mine[x][y] == '*':
                answer[x][y] = '*'

# 결과 출력
for row in answer:
    print(''.join(row))
