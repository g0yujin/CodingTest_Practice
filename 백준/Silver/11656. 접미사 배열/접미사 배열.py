import sys

word = sys.stdin.readline().strip()
word_list = []
for i in range(len(word)):
    temp = word[i:]
    word_list.append(temp)
word_list.sort()

for i in word_list:
    print(i)
