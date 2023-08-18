import sys
input = sys.stdin.readline

a = input().split('-')

for i in range(len(a)) :
    b = sum(map(int,a[i].split('+')))
    if i : ans -= b
    else : ans = b

print(ans)