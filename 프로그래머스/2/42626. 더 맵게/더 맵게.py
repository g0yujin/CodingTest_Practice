import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # scoville을 최소 힙으로 변환
    count = 0     # 음식을 섞은 횟수
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1  # 모든 스코빌 지수가 K 이상이 불가능한 경우
        
        # 가장 맵지 않은 두 음식 섞기
        temp1 = heapq.heappop(scoville)
        temp2 = heapq.heappop(scoville)
        new_scoville = temp1 + (temp2 * 2)
        
        heapq.heappush(scoville, new_scoville)
        count += 1
    
    return count