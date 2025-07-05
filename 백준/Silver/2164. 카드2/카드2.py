from collections import deque

n = int(input())
queue = deque(range(1, n+1))

while len(queue) > 1:
    queue.popleft()  # 맨 위 카드 버리기
    if queue:  # 큐가 비어있지 않다면
        queue.append(queue.popleft())  # 맨 위 카드를 맨 아래로

print(queue[0])