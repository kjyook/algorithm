import sys

n,m,k = map(int, sys.stdin.readline().split())

score = [[0,0] for _ in range(n)]

for i in range(n):
    tmpa, tmpb = map(int, sys.stdin.readline().split())
    score[i] = [tmpa,tmpb]

special = [[0,0] for _ in range(m+k)]

score.sort(key=lambda x: -x[1])
for i in range(k):
    special[i] = score[0]
    del score[0]

score.sort(key=lambda x: -x[0])
for i in range(m):
    special[i+k] = score[i]

total = 0

for i in special:
    total += i[0]

print(total)