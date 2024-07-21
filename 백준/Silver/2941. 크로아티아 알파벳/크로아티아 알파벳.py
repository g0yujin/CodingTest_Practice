croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
count = 0

for i in croatia:
    if i in word:
        count += word.count(i)
        word = word.replace(i, '.')

word = word.replace('.', '')
count += len(word)
print(count)