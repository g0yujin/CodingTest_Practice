import sys

N, X = map(int, sys.stdin.readline().split())
visited = list(map(int, sys.stdin.readline().strip().split()))

window_sum = sum(visited[:X])
result = [window_sum]

for i in range(X, N):
    window_sum += visited[i] - visited[i-X]
    result.append(window_sum)

max_visited = max(result)

if max_visited > 0:
    count = 0
    for i in result:
        if i == max_visited:
            count += 1
    print(max_visited)
    print(count)

else:
    print("SAD")
