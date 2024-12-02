import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

for idx, num in enumerate(number):
    if idx == 0:
        continue

    dp[idx] = (dp[idx - 1] + num) % m

count = [0] * m

for idx, num in enumerate(dp):
    if idx == 0:
        continue

    count[num] += 1

sum = count[0]

for i in count:
    if i > 1:
        sum += i * (i - 1) // 2

print(sum)