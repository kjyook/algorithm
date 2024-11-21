import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n) ]
people = []
answer = set()

def calculator():
    sum = 0

    for i in people:
        for j in people:
            sum += s[i][j]

    print(sum)
    answer.add(sum)
    return

def backtracking(a):
    if len(people) == n / 2:
        print(people)
        calculator()
        return
    
    for i in range(a, n):
        people.append(i)
        backtracking(i + 1)
        people.pop()

    return

backtracking(0)

print(answer)
while len(answer) != 2:
    answer.remove(max(answer))
    answer.remove(min(answer))

print(max(answer) - min(answer))