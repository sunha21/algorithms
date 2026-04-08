def solution(n, lost, reserve):
    lost_pe = 0    # 빌린 애들
    reserve_pe = len(reserve) # 일단 얘네는 체육을 할 수 있기는 한 애들
    own = n - len(set(lost + reserve)) # 그냥 딱 자기꺼 하나 있는애들
    lost2 = lost[:]
    
    reserve.sort()
    lost.sort()

    
    for x in lost2:
        if x in reserve:
            reserve.remove(x)
            lost.remove(x)
    
    for x in lost:
        if x - 1 in reserve:
            lost_pe += 1
            reserve.remove(x-1)
        
        elif x + 1 in reserve:
            lost_pe += 1
            reserve.remove(x+1)
            
    answer = reserve_pe + lost_pe + own
    return answer