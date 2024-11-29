import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

#dp[i][j]는  i번째 물건까지 고려했을때 무게 j를 채우는 가장 비싼 값을 나타낸다
#진행은 물건 기준으로 하고 해당 물건을 집어넣을때 각각들을 계산해준다.
dp = [[0] * (k + 1) for _ in range(n + 1)]

for idx, load in enumerate(bag):
    if idx == 0:
        continue

    for i in range(k + 1):
        if i < load[0]:
            dp[idx][i] = dp[idx - 1][i]
        else:
            dp[idx][i] = max(dp[idx - 1][i - load[0]] + load[1], dp[idx - 1][i])

print(dp[n][k])