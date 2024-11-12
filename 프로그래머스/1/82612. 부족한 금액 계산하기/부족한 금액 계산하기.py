def solution(price, money, count):
    
    total = 0
    for i in range(price, count*price+1, price):
        total += i
    
    if total > money:
        return total-money
    else:
        return 0