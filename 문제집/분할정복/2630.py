import sys
input = sys.stdin.readline

n = int(input())
box = [list(map(int, input().split())) for _ in range(n)]
sum_box = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_box[i][j] = sum_box[i - 1][j] + sum_box[i][j - 1] - sum_box[i - 1][j - 1]

blue, white = 0, 0

def dc(x1, y1, x2, y2):
    global sum_box, blue, white
    sum = sum_box[x2][y2] - sum_box[x1 - 1][y2] - sum_box[x2][y1 - 1] + sum_box[x1 - 1][y1 - 1]

    if sum == 0:
        white += 1
        return
    elif sum == (x2 - x1 + 1) * (x2 - x1 + 1):
        blue += 1
        return
    
    dc(x1,y1,(x1 + x2 - 1)//2,(y1 + y2 - 1)//2)
    dc(x1,(y1 + y2 + 1)//2,(x1 + x2 - 1)//2,y2)
    dc((x1 + x2 + 1)//2,y1,x2,(y1 + y2 - 1)//2)
    dc((x1 + x2 + 1)//2,(y1 + y2 + 1)//2,x2,y2)
    return


dc(1,1,n,n)
print(blue)
print(white)