import sys
input = sys.stdin.readline

def main():
    n = int(input())
    grape = [0]
    for _ in range(n):
        grape.append(int(input()))

    dp = [0] * (n + 1)

    dp[1] = grape[1]
    if n == 1:
        print(dp[1])
        return
    
    dp[2] = grape[1] + grape[2]
    if n == 2:
        print(dp[2])
        return
    
    dp[3] = max(grape[1] + grape[3], grape[2] + grape[3], dp[2])
    
    for i in range(4, n + 1):
        dp[i] = max(dp[i - 2] + grape[i], dp[i - 3] + grape[i - 1] + grape[i], dp[i - 1]) 

    print(max(dp))
    return

if __name__ == "__main__":
    main()