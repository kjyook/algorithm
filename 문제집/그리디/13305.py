import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = 1000000001
sum = 0

if n != 1:
    for i in range(n):
        if price[i] < min_price:
            min_price = price[i]

        if i == n - 1:
            break

        sum += min_price * distance[i]

print(sum)