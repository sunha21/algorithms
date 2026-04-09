def solution(left, right):
    
    nums = right - left + 1
    cnt = 0
    answer = 0
    
    for i in range(nums):
        num = left + i
        
        print(num)
        
        for j in range(1, int(num**0.5) + 1):
            if num % j == 0:
                cnt += 1
                if j != num // j:
                    cnt += 1  
        print(cnt)            
        
        if cnt % 2 == 0:
            answer += num
        else:
            answer -= num
        
        cnt = 0
    
    return answer