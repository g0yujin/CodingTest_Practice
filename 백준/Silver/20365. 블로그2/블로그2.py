import sys

N = int(sys.stdin.readline())
inputValue = sys.stdin.readline()

def solution(N, inputValue):

    colors = {"R": 0, "B": 0}
    colors[inputValue[0]] = 1

    for i in range(1, N):
        if inputValue[i] != inputValue[i - 1]:
            colors[inputValue[i]] += 1

    return min(colors["R"], colors["B"]) + 1

print(solution(N, inputValue))