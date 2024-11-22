import sys
input = sys.stdin.readline

t = int(input())
answer = [0] * 101
answer[1] = 1
answer[2] = 1
answer[3] = 1
answer[4] = 2
answer[5] = 2

for _ in range(t):
    n = int(input())
    for i in range(6, n + 1):
        answer[i] = answer[i - 5] + answer [i - 1]

    print(answer[n])
