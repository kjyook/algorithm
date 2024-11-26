import sys
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))

#dp[x][y] -> x번째 숫자의 최댓값이  y일때의 누적 counting
dp = [[0 for _ in range(51)] for _ in range(n + 1)]
dp[1][a[0]] = 1

for i in range(1, n + 1):
    if a[i - 1] > a[i]:
        dp[i] = dp [i - 1]
        if not dp[i][a[i]]:
            dp[i][a[i]] = 1
    elif a[i - 1] == a[i]:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1]
        for j in range(a[i] + 1):
            if not dp[i][j]:
                dp[i][j] += 1

print(max(dp[n]))
print(dp)