import sys

board = list(sys.stdin.readline().strip())
cnt_x = 0

# 덮을 수 없는 경우
cnt = board.count('X')
if cnt % 2 == 1:
    print(-1)
    sys.exit()

for i in range(0, len(board)):

    # 덮을 수 있는 경우
    if board[i] == 'X':
        cnt_x += 1

    if board[i] == '.':
        if cnt_x % 2 != 0: # X의 개수가 짝수이지만 홀수로 붙어있을 떄
            print(-1)
            sys.exit()
            
        if cnt_x == 2:      # BB인 경우
            board[i-2:i] = 'BB'
            cnt_x = 0

        elif cnt_x % 4 == 0: # AAAA인 경우
            board[i-cnt_x:i] = 'A' * cnt_x
            cnt_x = 0


        else:                # AAAA와 BB가 섞이는 경우
            board[i-cnt_x:i-2] = 'A' * (cnt_x-2)
            board[i-2:i] = 'BB'
            cnt_x = 0


    elif board[i] == 'X' and i == len(board)-1:
        if cnt_x == 2:      # BB인 경우
            board[i-1:i+1] = 'BB'

        elif cnt_x % 4 == 0: # AAAA인 경우
            board[i-(cnt_x-1):i+1] = 'A' * cnt_x

        elif cnt_x % 4 == 2:                # AAAA와 BB가 섞이는 경우
            board[i-(cnt_x-1):i-1] = 'A' * (cnt_x-2)
            board[i-1:i+1] = 'BB'


print(''.join(board))