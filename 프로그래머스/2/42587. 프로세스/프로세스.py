from collections import deque

def solution(priorities, location):
    queue =  [(i,j) for i,j in enumerate(priorities)] #(인덱스, 우선순위)
    answer = 0   # 몇 번째로 실행되는지
    
    while True:
        current = queue.pop(0)    # 큐에서 첫 번째 프로세스를 꺼냄
        # 나머지 큐에 현재 프로세스보다 우선순위가 높은 프로세스가 있으면 다시 큐에 넣기
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            answer += 1
            if current[0] == location:
                return answer
    