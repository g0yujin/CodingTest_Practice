import sys

S = list(sys.stdin.readline().rstrip())
i = 0
start = 0

while i < len(S):
    # '<' 가 나올 때 '>'가 나올 때까지
    if S[i] == '<':
        i += 1
        while S[i] != '>':
            i += 1

        i += 1     # 괄호가 끝나면 인덱스 +1

    elif S[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        while i < len(S) and S[i].isalnum():
            i += 1
        temp = S[start:i]
        temp.reverse()
        S[start:i] = temp

    else:   # 공백일 때는 인덱스 증가 = 건너뛰기
        i += 1

print(''.join(S))


