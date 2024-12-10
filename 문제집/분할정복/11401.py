import sys
input = sys.stdin.readline

n, k = map(int, input().split())
p = 1000000007

def factorial(a):
    sum = 1
    for i in range(2, a + 1):
        sum = (sum * i) % p

    return sum

def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    
    if b % 2 == 0:
        return power(a, b // 2) ** 2 % p
    else:
        return a * (power(a, (b - 1) // 2) ** 2) % p

up = factorial(n)
down = factorial(k) * factorial(n - k) % p

print(up * power(down, p - 2) % p)