def solution(n):
    fiv = [0, 1]

    for i in range(2, n+1):
        num = fiv[i - 1] + fiv[i - 2]
        fiv.append(num)
        
    answer = fiv[n] % 1234567
    return answer