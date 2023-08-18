n = int(input())
far = list(map(int,input().split()))
cost = list(map(int,input().split()))

answer = 0
m = cost[0]

for i in range(len(far)) :
    m = min(m, cost[i])
    answer += m * far[i]

print(answer)