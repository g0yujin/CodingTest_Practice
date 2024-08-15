import sys

time = 0
keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm']]

now_L, now_R = sys.stdin.readline().split()
word = list(sys.stdin.readline().rstrip())
x1, y1, x2, y2 = 0, 0, 0, 0

# 시작 위치 인덱스 찾기
for row in range(len(keyboard)):
    for col in range(len(keyboard[row])):
        if keyboard[row][col] == now_L:
            x1, y1 = row, col
        elif keyboard[row][col] == now_R:
            x2, y2 = row, col

    # 두 위치를 모두 찾은 경우 루프 종료
    if (x1, y1) != (0, 0) and (x2, y2) != (0, 0):
        break

for i in word:
    for row in range(len(keyboard)):
        for col in range(len(keyboard[row])):
            if keyboard[row][col] == i:
                if row <= 1:
                    # 왼손일 때
                    if col <= 4:
                        time += 1 + abs(x1 - row) + abs(y1 - col)
                        x1, y1 = row, col
                    # 오른손일 때
                    elif col >= 5:
                        time += 1 + abs(x2 - row) + abs(y2 - col)
                        x2, y2 = row, col

                elif row >= 2:
                    # 왼손일 때
                    if col <= 3:
                        time += 1 + abs(x1 - row) + abs(y1 - col)
                        x1, y1 = row, col
                    # 오른손일 때
                    elif col >= 4:
                        time += 1 + abs(x2 - row) + abs(y2 - col)
                        x2, y2 = row, col


print(time)
