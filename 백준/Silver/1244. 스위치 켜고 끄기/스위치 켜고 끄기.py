import sys

N = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
student = int(sys.stdin.readline())


for i in range(student):
    gender, switch_num = map(int, sys.stdin.readline().split())

    # 남학생일 때
    change_switch = []

    if gender == 1:
        # N보다 작은 switch_num배수 구하기
        for j in range(1, N+1):
            if j % switch_num == 0:
                change_switch.append(j)

        for k in change_switch:
            if switch[k-1] == 0:
                switch[k-1] = 1

            else:
                switch[k-1] = 0


    # 여학생일 때
    elif gender == 2:
        switch_num -= 1
        count = 0

        for l in range(1, N // 2 + 1):
            left_index = switch_num - l
            right_index = switch_num + l

            if left_index < 0 or right_index >= len(switch):
                break

            elif switch[left_index] == switch[right_index]:
                count = l

            else:
                break

        for m in range(switch_num - count, switch_num + count + 1):
            if switch[m] == 0:
                switch[m] = 1
            else:
                switch[m] = 0

for i in range(0, N, 20):
    print(*switch[i:i+20])

