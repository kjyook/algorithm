import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = [0] + list(map(int, input().split()))
prefix_sum = [0] * (n + 1)

for idx, s in enumerate(num):
    if idx == 0:
        continue

    prefix_sum[idx] = prefix_sum[idx - 1] + s

answer = set()

for idx, s in enumerate(prefix_sum):
    if idx < k:
        continue

    answer.add(s - prefix_sum[idx - k])

print(max(answer))