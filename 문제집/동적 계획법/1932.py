import sys
input = sys.stdin.readline

def main():
    n = int(input())
    triangle = [0] + [int(input()) for _ in range(n)]
    dp = [0] * 301

    if n == 1:
        print(triangle[1])
        return
    if n == 2:
        print(triangle[1] + triangle[2])
        return
    if n == 3:
        print(max(triangle[1], triangle[2]) + triangle[3])
        return

    dp[1] = triangle[1]
    dp[2] = triangle[1] + triangle[2]
    dp[3] = max(triangle[1], triangle[2]) + triangle[3]

    for i in range(4, n + 1):
        dp[i] = max(dp[i-3] + triangle[i-1], dp[i-2]) + triangle[i]

    print(dp[n])
    return

if __name__ == "__main__":
    main()