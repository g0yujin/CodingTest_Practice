n = int(input())
people = []

# 각 사람의 몸무게와 키 입력받기
for i in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height))

ranks = []

# 각 사람의 덩치 등수 계산
for i in range(n):
    rank = 1
    for j in range(n):
        # 자신보다 덩치가 큰 사람의 수를 세기
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    ranks.append(rank)

# 결과 출력
print(*ranks)