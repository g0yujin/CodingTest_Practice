remainder = []

for i in range(10):
    n = int(input())
    remainder.append(n % 42)

print(len(set(remainder)))
