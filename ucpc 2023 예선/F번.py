import sys

N, Q = map(int, input().split())

people = [[0]*N for _ in range(N)]
count = 1

for i in range(N):
    for j in range(N):
        people[i][j] = (i)*N + j+1

for _ in range(Q):
    temp = input().strip()
    if temp == "RO":
        for i in range(0, N, 2):
            people[i] = people[i][-1:] + people[i][:-1]  # 행 이동 최적화
    elif temp == "RE":
        for i in range(1, N, 2):
            people[i] = people[i][-1:] + people[i][:-1]  # 행 이동 최적화
    elif temp == "CO":
        for i in range(0, N, 2):
            column = [people[j][i] for j in range(N)]
            column = column[-1:] + column[:-1]
            for j in range(N):
                people[j][i] = column[j]  # 열 이동 최적화
    elif temp == "CE":
        for i in range(1, N, 2):
            column = [people[j][i] for j in range(N)]
            column = column[-1:] + column[:-1]
            for j in range(N):
                people[j][i] = column[j]  # 열 이동 최적화
    elif temp[0] == "S":
        dot = temp.split()
        r1, c1, r2, c2 = map(int, dot[1:])
        people[r1-1][c1-1], people[r2-1][c2-1] = people[r2-1][c2-1], people[r1-1][c1-1]  # "S" 연산 최적화
    else:
        print("error")

for i in range(N):
    print(*people[i])
