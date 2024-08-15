import sys

# 철수의 빙고판 2차원 배열
chulsu = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

# 사회자가 부르는 숫자 1차원
mc = []
for i in range(5):
    mc.extend(list(map(int, sys.stdin.readline().rstrip().split())))


order = 0

# 사회자가 부르는 숫자를 철수의 빙고판에서 0으로 만들기
for number in mc:
    for row in range(5):
        for col in range(5):
            if chulsu[row][col] == number:
                chulsu[row][col] = 0
                order += 1
                bingo_count = 0

                # 가로 빙고 확인
                for r in range(5):
                    if chulsu[r] == [0, 0, 0, 0, 0]:
                        bingo_count += 1

                # 세로 빙고 확인
                for c in range(5):
                    col_count = 0
                    for r in range(5):
                        if chulsu[r][c] == 0:
                            col_count += 1

                    if col_count == 5:
                        bingo_count += 1

                # 대각선 빙고 확인 \
                diag_count_1 = 0
                for r in range(5):
                    if chulsu[r][r] == 0:
                        diag_count_1 += 1
                if diag_count_1 == 5:
                    bingo_count += 1

                # 대각선 빙고 확인 /
                diag_count_2 = 0
                for r in range(5):
                    if chulsu[4-r][r] == 0:
                        diag_count_2 += 1
                if diag_count_2 == 5:
                    bingo_count += 1

                if bingo_count >= 3:
                    print(order)
                    sys.exit(0)


