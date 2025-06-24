import sys

while True:
    A, B, C = map(int, sys.stdin.readline().split())
    if A == 0:
        break
    else:
        if max(A, B, C) >= (A+B+C) - max(A, B, C):
            print("Invalid")
        elif A == B and B== C: # 세 변이 다 같은 경우
            print("Equilateral")
        elif A == B or B == C or A == C:
            print("Isosceles")

        elif A != B and B != C and A != C:
            print("Scalene")
