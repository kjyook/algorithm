import sys
input = sys.stdin.readline

n = int(input())
s = [0] + list(map(int, input().split()))
reverse_s = [s[0]] + s[1:][::-1]

up = [[0 for _ in range(max(s) + 1)] for _ in range(n + 1)]
down = [[0 for _ in range(max(s) + 1)] for _ in range(n + 1)]

for idx, num in enumerate(s):
    max_int = 0

    for i in range(1, idx):
        up[idx][s[i]] = up[idx - 1][s[i]]

        if s[i] < num and max_int < up[idx][s[i]]:
            max_int = up[idx][s[i]]

    if idx:
        up[idx][num] = max_int + 1

for idx, num in enumerate(reversed(s)):
    max_int = 0
    index = n - idx
    down[n][reverse_s[1]] = 1

    if idx == n:
        continue

    for i in range(1, idx + 1):
        down[index][reverse_s[i]] = down[index + 1][reverse_s[i]]

        if reverse_s[i] < num and max_int < down[index][reverse_s[i]]:
            max_int = down[index][reverse_s[i]]

    if idx:
        down[index][num] = max_int + 1

answer = set()
for i in range(1, n + 1):
    for j in s:
        answer.add(up[i][j] + down[i][j])

print(max(answer) - 1)