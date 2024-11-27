import sys
input = sys.stdin.readline

n = int(input())
line = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] 는 i번째 줄과 j번째 줄이 1-> 만난다 0 -> 안만난다.로 설정한다.
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
count = [0] * (n + 1)
answer = 0

#a와 b는 각각 전기줄의 시작점과 끝점을 담은 리스트의 형태
#return 0 -> 안만남 return 1 -> 만남
def check(a, b):
    if a[0] > b[0] and a[1] > b[1]:
        return 0
    if a[0] > b[0] and a[1] < b[1]:
        return 1
    if a[0] < b[0] and a[1] < b[1]:
        return 0
    if a[0] < b[0] and a[1] > b[1]:
        return 1

for i in range(1, n + 1):
    for j in range(1, i):
        if i == j:
            continue

        if check(line[i], line[j]):
            dp[i][j] += 1
            dp[j][i] += 1

for i in range(1, n + 1):
    count[i] = sum(dp[i])

while True:
    if sum(count) == 0:
        break

    idx = count.index(max(count))
    dp[idx] = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i][idx] = 0
        count[i] = sum(dp[i])
    
    answer += 1

print(answer)