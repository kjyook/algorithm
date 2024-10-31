import sys

N, K = map(int, sys.stdin.readline().split())
energy = list(map(int, sys.stdin.readline().split()))

a, b = 0, 1
answer = max(energy[a] - energy[b] - abs(a - b) * K, energy[b] - energy[a] - abs(b - a) * K)

while True:
    if energy[a] > energy[b]:
        diff = energy[a] - energy[b] - abs(a - b) * K
        answer = max(answer, diff)
    else:
        diff = energy[b] - energy[a] - abs(b - a) * K
        answer = max(answer, diff)

    b += 1
    if b>=N:
        a += 1
        b = a+1

print(answer)
