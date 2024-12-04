import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
count, sum = 0, 0

for c in reversed(coin):
    if c > (k - sum):
        continue

    temp = (k - sum) // c
    sum += (temp * c)
    count += temp

    if k == sum:
        break

print(count)