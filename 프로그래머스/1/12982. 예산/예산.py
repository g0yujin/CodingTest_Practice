def solution(d, budget):
    d.sort()
    ans = 0
    for i in d:
        if budget - i >= 0:
            budget -= i
            ans += 1
        else:
            break
    return ans