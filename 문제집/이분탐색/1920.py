import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

def binary_search(t):
    global a

    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == t:
            return 1
        if a[mid] < t:
            left = mid + 1
        if a[mid] > t:
            right = mid - 1

    return 0

for i in b:
    print(binary_search(i))