import sys

n, m = map(int, sys.stdin.readline().split())

d = [0] * (m+1)
d[1] = n

for i in range(2, m+1):
    d[i] = d[i-1] * (n-i+1) // i

print(int(d[m]))
