import sys
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))

#dp[x][y] -> x번째 숫자의 최댓값이  y인 수열의 누적 counting
dp = [[0 for _ in range(max(a) + 1)] for _ in range(n + 1)]

for idx, num in enumerate(a):
    max_int = 0

    for i in range(1, idx):
        dp[idx][a[i]] = dp[idx - 1][a[i]]

        if a[i] < num and max_int < dp[idx][a[i]]:
            max_int = dp[idx][a[i]]

    if idx:
        dp[idx][num] = max_int + 1

print(max(dp[n]))