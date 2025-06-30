import sys

vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    temp = True
    pwd = sys.stdin.readline().strip()
    if pwd == "end":
        break

    # 1. 모음 하나를 반드시 포함하여야 한다. = 하나라도 없으면 False
    if not any(vowel in pwd for vowel in vowels):
        temp = False

    # 2. 모음이 3개 or 자음이 3개 연속으로 오면 안된다
    if len(pwd) >= 3:
        for i in range(0, len(pwd)-2):
            current = pwd[i:i+3]
            count = 0
            for j in current:  # 모음인지 확인
                if j in vowels:
                    count += 1
                else:
                    count -= 1

            if count == 3 or count == -3:
                temp = False


    # 3. 같은 글자가 연속 2개 오면 안된다 (ee, oo 가능)
    for i in pwd:
        if i*2 in pwd:
            if i*2 == "ee" or i*2 == "oo":
                pass
            else:
                temp = False

    if temp:
        print(f'<{pwd}> is acceptable.')
    else:
        print(f'<{pwd}> is not acceptable.')