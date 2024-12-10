import sys
input = sys.stdin.readline

n, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
a = [[0]* n for _ in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] = A[i][j] % 1000

def matrix(k):
    global a, n
    if k == 1:
        return a
    
    if k % 2 == 0:
        temp = matrix(k // 2)
        return multiply(temp, temp)
    else:
        temp = matrix((k - 1) // 2)
        return multiply(multiply(temp, temp), a)

def multiply(lst_a, lst_b):
    global n
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for b in range(n):
                temp = (temp + lst_a[i][b] * lst_b[b][j]) % 1000

            answer[i][j] = temp
    
    return answer

print("\n".join(" ".join(map(str, row)) for row in matrix(b)))