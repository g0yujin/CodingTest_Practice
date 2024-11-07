T = int(input())

calender = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1, T+1):
    date = input()
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]

    if 0 < int(year) and 0 < int(month) <= 12 and 0 < int(day) <= calender[int(month)-1]:
        print(f'#{test_case} {year}/{month}/{day}')
    else:
        print(f'#{test_case} -1')
