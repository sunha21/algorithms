def solution(s):
    
    idx = 0
    answer = ''
    
    for ch in s:
        if (ch == ' '):
            answer += ' '
            idx = 0
        else:
            if (idx % 2 == 0):
                answer += ch.upper()
            else:
                answer += ch.lower()
            idx += 1
            
    return answer


# print(solution("a----------a----"))