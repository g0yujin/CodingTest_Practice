import sys

P, M = map(int, sys.stdin.readline().split())
rooms = []

for i in range(P):
    L, N = sys.stdin.readline().strip().split()
    L = int(L)  # 정수로 변환하고 저장

    # 들어갈 수 있는 방 찾기
    entered = False
    for room in rooms:
        base_level = room[0][0]

        # 레벨 범위 확인 & 방 정원 확인
        if (base_level - 10) <= L <= (base_level + 10) and len(room) < M:
            room.append((L, N))
            entered = True
            break

    # 들어갈 방이 없으면 새 방 생성
    if not entered:
        rooms.append([(L, N)])

# 결과 출력
for room in rooms:
    # 방 상태 출력
    if len(room) == M:
        print("Started!")
    else:
        print("Waiting!")

    # 플레이어 목록 (닉네임 순 정렬)
    room.sort(key=lambda x: x[1])
    for level, name in room:
        print(level, name)

