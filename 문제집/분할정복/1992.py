import sys
input = sys.stdin.readline

N = int(input())
box = [list(input()) for _ in range(N)]
answer = []

def quad_tree(n, x, y):
    global answer
    first = box[x][y]

    for i in range(n):
        for j in range(n):
            if first != box[x + i][y + j]:
                answer.append("(")
                quad_tree(n // 2, x, y)
                quad_tree(n // 2, x, y + n // 2)
                quad_tree(n // 2, x + n // 2, y)
                quad_tree(n // 2, x + n // 2, y + n // 2)
                answer.append(")")
                return

    answer.append(first)
    return

quad_tree(N, 0, 0)
print(''.join(answer))