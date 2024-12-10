import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]

answer = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        temp = 0

        for a in range(m):
            temp = temp + (A[i][a] * B[a][j])

        answer[i][j] = str(temp)

for i in answer:
    print(' '.join(i))