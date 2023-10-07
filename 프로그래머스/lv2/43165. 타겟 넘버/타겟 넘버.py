def solution(numbers, target):
    calc = [0]
    
    while numbers :
        tmp = []
        v = numbers.pop()
        
        for i in calc :
            tmp.append(i+v)
            tmp.append(i-v)
        calc = tmp

    answer = calc.count(target)
    
    return answer