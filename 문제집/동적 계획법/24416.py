import sys
input = sys.stdin.readline

n = int(input())
num = [0] * 100

def fib(a):
    return a-2

def fibonacci(a):
    num[1], num[2] = 1, 1
    for i in range(3, a + 1):
        num[i] = num[i - 1] + num[i - 2]

    return num[a]

print(fibonacci(n), fib(n))