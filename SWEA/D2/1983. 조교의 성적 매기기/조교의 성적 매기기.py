T = int(input())
result = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, T+1):
    N, K = map(int, input().split())
    term = N // 10
    d = {}

    for i in range(1, N+1):
        mid, end, project = map(int, input().split())
        score = mid*0.35 + end * 0.45 + project * 0.2

        # 딕셔너리에 학생의 번호와 점수를 같이 저장
        d[i] = score

    # 점수 기준 딕셔너리 정렬
    sorted_d = list(dict(sorted(d.items(), key=lambda x: x[1], reverse=True)))
    position = sorted_d.index(K) // term

    print(f'#{t} {result[position]}')


