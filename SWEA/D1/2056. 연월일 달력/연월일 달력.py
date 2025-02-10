T = int(input())

calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 31, 30, 31]

for t in range(1, T+1):
    date = input()

    year = date[0:4]
    month = date[4:6]
    day = date[6:8]

    if int(year) > 0 and 0 < int(month) <= 12  and 0 < int(day) <= calendar[int(month)-1]:
        print(f'#{t} {year}/{month}/{day}')
    else:
        print(f'#{t} -1')
