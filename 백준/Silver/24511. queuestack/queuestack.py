from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
check = list(map(int, input().split()))
arr = list(map(int, input().split()))
m = int(input())
inputArr = list(map(int, input().split()))

queue = deque()

for i in range(n) :
    if check[i] == 0 :
        queue.appendleft(arr[i])

for n in inputArr :
    queue.append(n)
    print(queue.popleft(), end=' ')