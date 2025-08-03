import sys

s = sys.stdin.readline().strip()
n = len(s)
a = s.count('a')

s += s[0:a-1]   # 원형 문자열

min_val = float('inf')
for i in range(n):
    min_val = min(min_val, s[i:i+a].count('b'))
print(min_val)

