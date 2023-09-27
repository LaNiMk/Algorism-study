def solution(cacheSize, cities):
    cache = []
    answer = 0
    
    for i in range(len(cities)) :
        cities[i] = cities[i].lower()
    
    if cacheSize == 0 :
        answer = len(cities) * 5
    
    else :
        for city in cities :
            if not city in cache : 
                answer += 5
                if len(cache) < cacheSize:
                    cache.append(city)
                else:
                    cache.pop(0)
                    cache.append(city)     
            else:
                answer += 1
                cache.pop(cache.index(city))
                cache.append(city)
    
    return answer
            