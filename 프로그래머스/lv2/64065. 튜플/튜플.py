def solution(s):
    answer = []
    s = list(s.replace('{','').replace('}', '').split(','))
    
    count = {}
    for i in s :
        count[int(i)] = count.get(int(i), 0) + 1
        
    answer = sorted(count, key = lambda x : count[x], reverse = True)
    return answer