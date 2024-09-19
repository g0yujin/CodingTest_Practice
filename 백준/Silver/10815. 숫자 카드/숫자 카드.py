import sys

N = int(sys.stdin.readline()) # 상근이의 숫자 카드 개수
card_n = set(map(int, sys.stdin.readline().split())) # N개의 숫자
M = int(sys.stdin.readline()) # 주어진 숫자 카드 개수
card_m = list(map(int, sys.stdin.readline().split())) # M개의 숫자


for i in range(M):
    if card_m[i] in card_n:
        card_m[i] = 1
    else:
        card_m[i] = 0

print(*card_m)

