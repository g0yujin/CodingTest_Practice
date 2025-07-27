import sys, heapq

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    row = list(map(int, sys.stdin.readline().strip().split()))

    if i == 0:
        heap = row[:]
        heapq.heapify(heap)

    else:
        for j in row:
            if j > heap[0]:
                heapq.heapreplace(heap, j)

print(heap[0])





