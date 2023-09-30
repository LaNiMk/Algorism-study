def solution(clothes):
    count = {}
    for cloth in clothes :
        count[cloth[1]] = count.get(cloth[1], 0) + 1
    
    cnt = 1
    for i in count.values() :
        cnt *= (i+1)
    
    return (cnt - 1)