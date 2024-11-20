import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = []

def backtracking(a):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(a, n + 1):
        answer.append(i)
        backtracking(i)
        answer.pop()

    return

backtracking(1)