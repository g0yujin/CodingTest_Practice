import heapq

def solution(jobs):
    now_time = 0 # 현재 시간
    heap = []    # 현재 수행 가능한 작업
    finish = 0   # 완료한 작업
    before_request = -1
    total_time= 0   # 총 걸린시간
    
    while finish < len(jobs):  # 작업이 다 끝날 때까지 반복
        # 현재 시간 기준 수행 가능한 작업들(= 현재시점(now_time) > 작업 요청 시점)을 힙에 추가
        for job in jobs:
            if before_request < job[0] <= now_time: #[소요시간, 작업 요청 시점]
                heapq.heappush(heap, [job[1], job[0]])  # 위치 바꿔 넣기
        
        # 작업할 게 있다면
        if len(heap) > 0:
            now_working = heapq.heappop(heap)  # 소요시간이 가장 작은 애 꺼내기
            before_request = now_time
            now_time += now_working[0]   # 일 끝남
            total_time += (now_time - now_working[1])  # 이 작업이 대기하고 끝날때까지 걸린 시간
            finish += 1
            
        else:  # 수행할 작업이 없으면
            now_time += 1
            
    answer = int(total_time / len(jobs))
    return answer   