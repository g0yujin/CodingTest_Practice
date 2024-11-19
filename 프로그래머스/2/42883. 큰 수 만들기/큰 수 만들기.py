def solution(number, k):
    stack = []
    for num in number:
        # 스택이 비어있지 않고, k가 남아있고, 스택의 마지막 수가 현재 수보다 작으면
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
        
    # k가 남아있는 경우 뒤에서부터 제거
    if k != 0:
        stack = stack[:-k]
        
    return ''.join(stack)