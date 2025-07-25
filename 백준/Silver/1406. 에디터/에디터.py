import sys

word = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline())

# 두 스택으로 분리
left = word  # 커서 왼쪽
right = []  # 커서 오른쪽

for i in range(M):
    command = sys.stdin.readline().strip().split()

    if command[0] == 'L':
        if left:
            right.append(left.pop())  # 왼쪽 → 오른쪽

    elif command[0] == 'D':
        if right:
            left.append(right.pop())  # 오른쪽 → 왼쪽

    elif command[0] == 'B':
        if left:
            left.pop()  # 왼쪽에서 삭제

    elif command[0] == 'P':
        left.append(command[1])  # 왼쪽에 추가

# 결과: 왼쪽 + 오른쪽 뒤집기
result = left + right[::-1]
print(''.join(result))