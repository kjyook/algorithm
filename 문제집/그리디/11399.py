import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
time.sort()
sum = 0

for idx, t in enumerate(time):
    sum = sum + (n - idx) * t

print(sum)