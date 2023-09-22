def solution(arr1, arr2):
    n, m, k = len(arr1), len(arr2), len(arr2[0])
    
    answer = [[0]*k for _ in range(n)]
    
    for x in range(n) :
        for y in range(k) :
            for z in range(m) :
                answer[x][y] += arr1[x][z] * arr2[z][y]
                
    return answer