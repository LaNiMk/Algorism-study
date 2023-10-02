def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    arr1 = []
    arr2 = []
    
    for i in range(len(str1)-1) :
        word1 = str1[i:i+2]
        if word1.isalpha() : 
            arr1.append(word1)
    
    for j in range(len(str2)-1) :
        word2 = str2[j:j+2]
        if word2.isalpha() :
            arr2.append(word2)
    
    print(arr1, arr2)
    
    if not arr1 and not arr2 :
        return 65536
    
    else :
        plus = []
        cross = []

        for k in arr1 :
            if k in arr2 :
                arr2.remove(k)
                cross.append(k)
        
        plus = arr1 + arr2
        
        answer = (len(cross) / len(plus)) * 65536
        return int(answer)