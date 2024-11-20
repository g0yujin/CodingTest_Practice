def solution(people, limit):
    people.sort()  # 오름차순 정렬

    answer = 0
    left = 0
    right = len(people) - 1

    while left <= right:
        if left == right:  # 혼자 남은 경우
            answer += 1
            break

        if people[left] + people[right] <= limit:  # 두 명이 같이 탈 수 있는 경우
            left += 1
            right -= 1
        else:  # 무거운 사람 혼자 타야 하는 경우
            right -= 1
        answer += 1

    return answer