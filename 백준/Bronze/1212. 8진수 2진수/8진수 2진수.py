# 입력 받은 수 -> 10진수 -> 2진수로 바꾸기

N = input()

ten = (int(N, 8))
print(bin(ten).replace('0b', ''))
