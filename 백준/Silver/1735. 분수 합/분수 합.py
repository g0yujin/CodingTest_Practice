import sys
import math

A1, B1 = map(int, sys.stdin.readline().split())
A2, B2 = map(int, sys.stdin.readline().split())

numerator = (A1*B2) + (A2*B1)
denominator = B1 * B2

gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd

print(numerator, denominator)