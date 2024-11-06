def solution(wallet, bill):
    count = 0
    
    while True:   # min끼리 비교, max끼리 비교 둘다 bill의 값이 작아야됨
        if min(wallet) >= min(bill) and max(wallet) >= max(bill):
            return count
        else:   # 지갑에 지폐가 안 들어갈 때
            if bill[0] >= bill[1]:
                bill[0] //= 2
                count += 1
            else:
                bill[1] //= 2
                count += 1
            