import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n) ]
everyone = set(i for i in range(n))
people = set()
other = set()
min = sum(sum(row) for row in s)

def calculator():
    global min
    sum_p, sum_o = 0, 0
    other = everyone - people

    for i in people:
        for j in people:
            sum_p += s[i][j]
        
    for i in other:
        for j in other:
            sum_o += s[i][j]

    if min > abs(sum_o - sum_p):
        min = abs(sum_o - sum_p)

    return

def backtracking(a):
    if len(people) == n / 2:
        calculator()
        return
    
    for i in range(a, n):
        people.add(i)
        backtracking(i + 1)
        people.remove(i)

    return

backtracking(0)

print(min)