import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
minus, zero, plus = 0, 0, 0

def nine_tree(n, x, y):
    global minus, zero, plus
    first = paper[x][y]

    for i in range(n):
        for j in range(n):
            if first != paper[x + i][y + j]:
                nine_tree(n // 3, x, y)
                nine_tree(n // 3, x, y + n // 3)
                nine_tree(n // 3, x, y + n // 3 * 2)
                nine_tree(n // 3, x + n // 3, y)
                nine_tree(n // 3, x + n // 3, y + n // 3)
                nine_tree(n // 3, x + n // 3, y + n // 3 * 2)
                nine_tree(n // 3, x + n // 3 * 2, y)
                nine_tree(n // 3, x + n // 3 * 2, y + n // 3)
                nine_tree(n // 3, x + n // 3 * 2, y + n // 3 * 2)
                return
            
    if first == 0:
        zero += 1
    elif first == 1:
        plus += 1
    else:
        minus += 1

    return

nine_tree(N, 0, 0)
print(minus, zero, plus, sep="\n")