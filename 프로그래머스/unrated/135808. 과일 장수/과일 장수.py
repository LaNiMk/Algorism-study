def solution(k, m, score):
    score.sort()
    box_min = score[-1]
    answer = 0
    
    while True :
        if len(score) >= m :
            for i in range(m) :
                num = score.pop()
                box_min = min(num, box_min)
            answer += (box_min * m)
        else :
            break
    return answer