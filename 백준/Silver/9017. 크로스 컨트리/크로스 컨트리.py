import sys

T = int(sys.stdin.readline())

for test_case in range(T):
    N = int(sys.stdin.readline())
    people = list(map(int, sys.stdin.readline().split()))

    # 점수 계산에서 제외되는 팀 구하기
    no_rank = []
    for i in range(1, max(people) + 1):
        if people.count(i) < 6:
            no_rank.append(i)

    # 점수 부여하기
    scores = []
    score = 1
    for i in range(N):
        if people[i] in no_rank:
            scores.append(0)
        else:
            scores.append(score)
            score += 1

    # 각 팀별 점수 저장
    team_scores = {}

    for i in range(N):
        if people[i] in no_rank:
            continue

        team_num = people[i]
        if team_num not in team_scores:
            team_scores[team_num] = []
        team_scores[team_num].append(scores[i])

    # 각 팀의 상위 4명 점수 합계와 5번째 선수 점수 계산
    team_results = {}

    for team, score_list in team_scores.items():
        if len(score_list) >= 6:  # 6명 이상인 팀만 고려
            # 상위 4명의 점수 합
            top4_sum = sum(sorted(score_list)[:4])
            # 5번째 선수의 점수 (타이브레이커)
            fifth_score = sorted(score_list)[4]
            team_results[team] = (top4_sum, fifth_score)

    # 우승팀 결정
    # 1순위: 상위 4명 점수 합이 가장 낮은 팀
    # 2순위: 동점일 경우 5번째 선수 점수가 가장 낮은 팀
    winner = min(team_results.keys(), key=lambda x: (team_results[x][0], team_results[x][1]))

    print(winner)