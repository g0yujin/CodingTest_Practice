import sys

N = int(sys.stdin.readline())
price = []
for i in range(N):
    price.append(int(sys.stdin.readline()))

price.sort(reverse=True)

discount = sum(price[2:N:3])    # 할인받는 값

print(sum(price) - discount)