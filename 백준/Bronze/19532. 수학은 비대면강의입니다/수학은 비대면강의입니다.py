import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

x = ((c * e) - (f * b)) // ((a * e) - (d * b))

y = ((c * d) - (a * f)) // ((b * d) - (a * e))



print(x, y)