import sys
input = sys.stdin.readline

n = int(input())
# 아 이거 동적으로 할당했을때 안된 이유가 n=1일때를 설정을 안해줘서다... 꼼곰히 체크하자.,!
dp = [0] * (n + 1)

if n == 1:
    print(0)
elif n == 2:
    print(1)
elif n == 3:
    print(1)
else:
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n + 1):
        if i % 2 == 0 and i % 3 == 0:
            dp[i] = min(dp[i//2], dp[i//3], dp[i - 1]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i - 1]) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[i//3], dp[i - 1]) + 1
        else:
            dp[i] = dp[i - 1] + 1

    print(dp[n])