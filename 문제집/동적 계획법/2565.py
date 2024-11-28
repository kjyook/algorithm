import sys
input = sys.stdin.readline

n = int(input())
line = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
line.sort()

#dp는 x번째까지 수열에서 최대가 y인 수열의 길이를 나타내는 리스트이다.
dp = [[0 for _ in range(501)] for _ in range(101)]
check = set()

for idx, l in enumerate(line):
    if idx == 0:
        continue

    max_int = 0

    for i in range(1, idx):
        dp[idx][line[i][1]] = dp[idx - 1][line[i][1]]
    
        if line[i][1] < l[1] and max_int < dp[idx][line[i][1]]:
            max_int = dp[idx][line[i][1]]

    dp[idx][l[1]] = max_int + 1

print(n - max(dp[n]))