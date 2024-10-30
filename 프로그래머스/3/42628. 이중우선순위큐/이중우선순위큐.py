import heapq
def solution(operations):
    answer = []
    heap = []
    for o in operations:
        current = o.split()
        if current[0] == 'I':
            current_num = int(current[1])
            heapq.heappush(heap,current_num)
        else : 
            if len(heap) ==  0 : 
                pass
            # 최대힙 제거 
            elif current[1] == "1" : 
                heap = heapq.nlargest(len(heap),heap)[1:]
                heapq.heapify(heap)
                
            # 최소힙 제거
            else : 
                heapq.heappop(heap)
    if heap : 
        answer.append(max(heap))
        answer.append(min(heap))
    else : 
        answer = [0,0]

    return answer