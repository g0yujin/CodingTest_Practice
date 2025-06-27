P = int(input())

for _ in range(P):
    data = list(map(int, input().split()))
    T = data[0]  # 테스트 케이스 번호
    heights = data[1:]  # 학생들의 키

    count = 0  # 뒤로 물러나는 횟수
    line = []  # 현재 줄서기 상태

    for height in heights:
        # 현재 학생보다 키가 큰 학생들의 개수를 센다
        # 이들이 모두 뒤로 물러나야 함
        step_back = 0
        for i in range(len(line)):
            if line[i] > height:
                step_back += 1

        count += step_back

        # 현재 학생을 적절한 위치에 삽입
        inserted = False
        for i in range(len(line)):
            if line[i] > height:
                line.insert(i, height)
                inserted = True
                break

        if not inserted:
            line.append(height)

    print(T, count)