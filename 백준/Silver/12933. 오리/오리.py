import sys

sound = list(sys.stdin.readline().rstrip())
quack = 'quack'
visited = [False] * len(sound)  # 처리된 문자열인지, False: 처리 전, True: 처리 후
duck = 0  # 최소 오리 수
idx = 0

if len(sound) % 5 != 0:
    print(-1)
    exit()

else:
    for i in range(len(sound)):
        # q가 첫 시작이고 아직 처리전 문자일 때
        if sound[i] == 'q' and not visited[i]:
            first = True  # quack의 시작

            for i in range(len(sound)):
                if quack[idx] == sound[i] and not visited[i]:
                    visited[i] = True

                    if sound[i] == 'k':
                        if first:
                            duck += 1
                            first = False
                        idx = 0
                        continue
                    idx += 1

    if duck == 0 or not all(visited):
        print(-1)
    else:
        print(duck)



