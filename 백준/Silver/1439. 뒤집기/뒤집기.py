s = input()

cnt = 0
a, b = 0, 0

for i in range(len(s)) :
        if s[i] == '1' :
            a += 1
            if i != 0 and s[i-1] == '1' :
                a -= 1

for i in range(len(s)) :
    if s[i] == '0' :
        b += 1
        if i != 0 and s[i-1] == '0' :
            b -= 1
    
cnt = min(a, b)

print(cnt)