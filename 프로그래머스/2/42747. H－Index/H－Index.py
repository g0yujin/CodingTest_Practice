def solution(citations):
    citations.sort(reverse=True)  # 인용 수를 내림차순으로 정렬
    for h in range(len(citations)):
        # h+1 편의 논문이 h+1번 이상 인용된 경우
        if citations[h] < h + 1:
            return h
    return len(citations)
