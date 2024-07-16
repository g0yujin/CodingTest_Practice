student = []
for i in range(1, 31):
    student.append(i)

for j in range(28):
    n = int(input())
    student.remove(n)

student.sort()
print(*student, sep='\n')
