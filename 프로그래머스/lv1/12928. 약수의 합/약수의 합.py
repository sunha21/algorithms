def solution(n):
    sum = 0
    
    for i in range(n):
        i += 1
        if (n % i == 0):
            sum += i
    return sum