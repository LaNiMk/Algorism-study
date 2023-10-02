n = int(input())
answer = 0

for i in range(n) :
    check = []
    s = input()
    answer += 1
    for j in s :
        if j not in check :
            check.append(j)
        elif j in check and check[-1] == j :
            continue
        else :
            answer -= 1
            break

print(answer)
