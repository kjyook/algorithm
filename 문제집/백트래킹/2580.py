import sys
input = sys.stdin.readline

num = [list(map(int, input().split())) for _ in range(9) ]
flag = False

def guess(x, y):
    one_to_ten = set(i+1 for i in range(9))
    row = set(num[x])
    col = set()

    for i in range(9):
        if num[i][y] != 0:
            col.add(num[i][y])

    box = set()
    start_row = (x // 3) * 3
    start_col = (y // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if num[i][j]:
                box.add(num[i][j])

    possible = one_to_ten - row - col - box

    return possible

def sudoqu(x, y):
    global flag

    if x == 9:
        for i in num:
            print(' '.join(map(str, i)))
        flag = True
        return
        
    if flag:
        return

    if num[x][y] == 0:
        a = guess(x, y)
        
        for i in a:
            num[x][y] = i
        
            if y != 8:
                sudoqu(x, y + 1)
            else:
                sudoqu(x + 1, 0)

        num[x][y] = 0
    else:
        if y != 8:
            sudoqu(x, y + 1)
        else:
            sudoqu(x + 1, 0)

    return

sudoqu(0,0)