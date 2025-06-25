import sys

N = int(sys.stdin.readline())
channel_list = []
for i in range(N):
    channel_list.append(sys.stdin.readline().strip())


# KBS1과 KBS2를 직접 움직이기
answer = ''
one = channel_list.index('KBS1')
two = channel_list.index('KBS2')
if one > two:
    two += 1
    
# KBS1로 이동
answer += '1' * one

# KBS1 옮기기
answer += '4' * one

# KBS2로 이동
answer += '1' * two

# KBS2 올리기
answer += '4' * (two-1)

print(answer)
