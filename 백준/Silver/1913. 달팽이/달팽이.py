import sys

N = int(sys.stdin.readline())
number = int(sys.stdin.readline())

# 초기 표
snail = [[0] * N for _ in range(N)]

# 시작 위치 (정가운데)
x, y = N // 2, N // 2
snail[x][y] = 1

# 방향: 위, 오른쪽, 아래, 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
num = 2  # 시작 숫자
loop = 1  # 현재 루프에서 이동해야 할 거리
direction_index = 0  # 현재 방향

answer = [x + 1, y + 1]  # 초기값 설정

# 달팽이 그리기
while num <= N * N:
    for _ in range(2):  # 같은 거리로 두 방향 이동
        for _ in range(loop):
            x += dx[direction_index]
            y += dy[direction_index]

            # 범위를 벗어나지 않는지 확인
            if 0 <= x < N and 0 <= y < N:
                snail[x][y] = num

                if number == num:
                    answer = [x + 1, y + 1]

                num += 1  # 여기서 num 증가

            # 모든 숫자를 채우면 루프 종료
            if num > N * N:
                break

        if num > N * N:
            break

        # 방향 전환
        direction_index = (direction_index + 1) % 4

    # 루프가 끝나면 이동할 거리 증가
    loop += 1

# 배열 출력 
for row in snail:
    print(*row)

print(*answer)
