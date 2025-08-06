import sys, string

N = int(sys.stdin.readline())

used = set()

for i in range(N):
    words = sys.stdin.readline().strip().split()

    found = False
    # 1단계 - 각 단어 첫번째 글자 확인
    for idx, word in enumerate(words):
        if word[0].lower() not in used:
            used.add(word[0].lower())
            words[idx] = f'[{word[0]}]{word[1:]}'
            found = True
            break

    # 2단계 - 처음부터 모든 글자 확인
    if not found:
        for word_idx, word in enumerate(words):
            for char_idx, char in enumerate(word):
                if char.isalpha() and char.lower() not in used:
                    used.add(char.lower())
                    # 해당 단어만 수정
                    words[word_idx] = word[:char_idx] + f'[{char}]' + word[char_idx + 1:]
                    found = True
                    break
            if found:  # 이중 루프 탈출
                break

        # 한 번만 출력
    print(' '.join(words))