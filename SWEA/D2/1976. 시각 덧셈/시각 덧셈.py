T = int(input())

for test_case in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    m = m1 + m2

    if m >= 60:
        h += m // 60
        m = m % 60
    if h > 12:
        h -= 12
    print(f'#{test_case} {h} {m}')