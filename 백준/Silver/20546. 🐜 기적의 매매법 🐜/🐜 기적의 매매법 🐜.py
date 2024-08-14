import sys

cash = int(sys.stdin.readline())
stock_price = list(map(int, sys.stdin.readline().split()))

# 준현이의 주식 매수
j_cash = cash
j_stock, j_assets = 0, 0

for i in stock_price:
    if i <= j_cash:
        j_stock = j_cash // i   # 몫 = 주식 수
        j_cash = j_cash % i     # 나머지 = 남은 자산
    else:
        pass

# 준현이의 자산
j_assets = stock_price[-1] * j_stock + j_cash

# 성민이의 주식 매수
s_cash = cash
s_stock, s_assets = 0, 0
up, down = 0, 0

for i in range(len(stock_price)):
    if i > 0:
        # 3일 연속 상승하면 전량 매도
        if stock_price[i-1] < stock_price[i]:
            up += 1
            down = 0
            if up == 3:
                s_cash += s_stock * stock_price[i]
                s_stock = 0
                up = 0

        # 3일 연속 하락하면 전량 매수
        elif stock_price[i-1] > stock_price[i]:
            down += 1
            up = 0

            if down >= 3:
                s_stock += s_cash // stock_price[i]
                s_cash = s_cash % stock_price[i]

        elif stock_price[i-1] == stock_price[i]:
            down = 0
            up = 0


# 성민이의 자산
s_assets = stock_price[-1] * s_stock + s_cash

if j_assets > s_assets:
    print('BNP')
elif j_assets < s_assets:
    print('TIMING')
elif j_assets == s_assets:
    print('SAMESAME')
