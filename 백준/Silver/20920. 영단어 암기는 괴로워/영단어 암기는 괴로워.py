import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
words = []

for _ in range(n):
    word = input().strip()
    if len(word) >= m:  # 길이가 M 이상인 단어만
        words.append(word)

# 단어별 빈도 계산
word_count = Counter(words)

sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], -len(x), x))

for word in sorted_words:
    print(word)
