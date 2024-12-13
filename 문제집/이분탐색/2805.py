import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))
height.sort()

left, right = 0, height[-1]

while left <= right:
    sum = 0
    mid = (left + right) // 2

    for i in reversed(height):
        if i <= mid:
            break
        else:
            sum += (i - mid)

    if sum == m:
        print(mid)
        break
    elif sum < m:
        right = mid - 1
    else:
        left = mid + 1

    if left > right:
        mid = (left + right) // 2
        print(mid)
        break