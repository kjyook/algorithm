import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = []

def backtracking(a):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(a, n+1):
        if i not in answer:
            answer.append(i)
            backtracking(i+1)
            answer.pop()

    return

backtracking(1)