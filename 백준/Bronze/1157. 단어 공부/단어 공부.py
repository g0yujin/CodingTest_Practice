import sys

word = sys.stdin.readline().rstrip().upper()

word_set = list(set(word))
count_list = []

for x in word_set:
    count = word.count(x)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print("?")

else:
    print(word_set[(count_list.index(max(count_list)))])


