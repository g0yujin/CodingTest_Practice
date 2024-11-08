T = int(input())

for i in range(T):
    A, B, N = map(int, input().split())
    cnt = 0

    while True:
        if A > N or B > N:
            print(cnt)
            break
        else:
            if A > B:
                B += A
                cnt += 1
            else:
                A += B
                cnt += 1