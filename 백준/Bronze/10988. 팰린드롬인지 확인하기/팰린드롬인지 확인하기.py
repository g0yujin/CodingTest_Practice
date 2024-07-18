import sys

word = list(map(str, sys.stdin.readline().rstrip()))

if word == list(reversed(word)):
    print(1)
else:
    print(0)