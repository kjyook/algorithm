import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

for x_idx, line in enumerate(number):
    for y_idx, num in enumerate(line):
        dp[x_idx + 1][y_idx + 1] = dp[x_idx + 1][y_idx] + num

def calcul():
    global dp
    x1, y1, x2, y2 = map(int, input().split())
    sum = 0

    for i in range(x1, x2 + 1):
        sum += (dp[i][y2] - dp[i][y1 - 1])

    print(sum)
    return

for _ in range(m):
    calcul()