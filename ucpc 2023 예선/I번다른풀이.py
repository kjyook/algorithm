import sys

N, K = map(int, sys.stdin.readline().split())
dp = list(map(int, sys.stdin.readline().split()))

front = [0]*N
back = [0]*N

for i in range(N):
    front[i] = dp[i] + K*i
    back[i] = dp[i] + K*(N-i)

max = 0
min = 0

for i in range(N):
    if front[i] > front[max]:
        max = i
    if front[i] < front[min] and i > max:
        min = i
answer = front[max] - front[min]

min = N-1
max = N-1
for i in range(N):
    if back[N-1-i] > back[max]:
        max = N-1-i
    if back[N-1-i] < back[min] and N-1-i < max:
        min = N-1-i

answer2 = back[max] - back[min]

print(answer,answer2)