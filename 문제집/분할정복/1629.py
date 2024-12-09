import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def qc(n):
    global a, b, c
    if n == 1:
        return a % c

    if n % 2 == 0:
        return qc(n // 2) ** 2 % c
    else:
        return a * (qc((n - 1) // 2) ** 2) % c

print(qc(b))