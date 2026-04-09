def solution(price, money, count):
    
    money_need = 0
    
    for i in range(count):
        n = i + 1
        money_need += price * n
        

    answer = money_need - money
    
    if answer < 0:
        return 0
    
    return answer