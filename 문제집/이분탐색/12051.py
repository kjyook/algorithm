import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [A[0]]

def findIndex(k):
    start, end = 0, len(dp) - 1

    while start <= end:
        mid = (start + end) // 2

        if dp[mid] == k:
            return mid
        elif dp[mid] < k:
            start = mid + 1
        else:
            end = mid - 1

    return start
    
for i in A:
    if dp[-1] < i:
        dp.append(i)
    elif dp[-1] == i:
        continue
    else:
        idx = findIndex(i)
        dp[idx] = i

print(len(dp))