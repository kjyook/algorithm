import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

left, right = 1, k

while left <= right:
    mid = (left + right) // 2

    sum = 0
    for i in range(1, n + 1):
        sum += min(mid // i, n)
    
    if sum >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)