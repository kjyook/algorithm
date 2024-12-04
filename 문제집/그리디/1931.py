import sys
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
count = 0
time.sort(key=lambda x:(x[1], x[0]))
last_time = 0

for t in time:
    if last_time <= t[0]:
        count += 1
        last_time = t[1]

print(count)