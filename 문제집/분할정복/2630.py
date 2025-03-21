import sys
input = sys.stdin.readline

N = int(input())
box = [list(map(int, input().split())) for _ in range(N)]
blue, white = 0, 0

def quad_tree(n, x, y):
    global blue, white
    first = box[x][y]

    for i in range(n):
        for j in range(n):
            if first != box[x+i][y+j]:
                quad_tree(n // 2, x, y)
                quad_tree(n // 2, x + n // 2, y)
                quad_tree(n // 2, x, y + n // 2)
                quad_tree(n // 2, x + n // 2, y + n // 2)
                return

    if first == 0:
        white += 1
    else:
        blue += 1

    return

quad_tree(N, 0, 0)
print(white, blue, sep="\n")