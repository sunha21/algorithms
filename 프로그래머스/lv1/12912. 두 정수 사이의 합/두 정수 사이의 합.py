def solution(a, b):
    n = abs(a - b) + 1
    m = min(a, b)
    sum = 0
    
    for i in range(n):
        sum += m
        m += 1
        
    return sum