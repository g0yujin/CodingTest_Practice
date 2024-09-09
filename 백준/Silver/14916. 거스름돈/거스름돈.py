import sys

coin = int(sys.stdin.readline())
cnt = 0 # 동전 개수

while True:
    if coin % 5 == 0:  # 5원으로만 거슬러 주는 경우
        cnt += coin // 5
        break
    else:
        coin -= 2
        cnt += 1

    if coin < 0:
        print(-1)
        sys.exit()

print(cnt)