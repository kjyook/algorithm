import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

def calcul_dp(x, y):
    global b_dp, w_dp

    b = b_dp[x][y] - b_dp[x - k][y] - b_dp[x][y - k] + b_dp[x - k][y - k]
    w = w_dp[x][y] - w_dp[x - k][y] - w_dp[x][y - k] + w_dp[x - k][y - k]

    return min(b, w)

#1018번 문제와 커플문제이다. 그때는 브루트포스로 풀었는데 이번에는 메모리는 늘었지만 시간이 절반으로 줄었다. 아마도 불가능할듯?
chess = [input().rstrip() for _ in range(n)]
w_chess = [[0] * m for _ in range(n)]
b_chess = [[0] * m for _ in range(n)]

#일단 체스판 뒤집어야 하는거 count해주고
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            if chess[i][j] == "W":
                b_chess[i][j] = 1
            else:
                w_chess[i][j] = 1
        else:
            if chess[i][j] == "B":
                b_chess[i][j] = 1
            else:
                w_chess[i][j] = 1

w_dp = [[0] * (m + 1) for _ in range(n + 1)]
b_dp = [[0] * (m + 1) for _ in range(n + 1)]

#2dlist prefix sum은 사각형 분할하여 계산
for i in range(n):
    for j in range(m):
        w_dp[i + 1][j + 1] = w_dp[i + 1][j] + w_dp[i][j + 1] - w_dp[i][j] + w_chess[i][j]
        b_dp[i + 1][j + 1] = b_dp[i + 1][j] + b_dp[i][j + 1] - b_dp[i][j] + b_chess[i][j]

answer = set()
for i in range(k, n + 1):
    for j in range(k, m + 1):
        answer.add(calcul_dp(i, j))

print(min(answer))