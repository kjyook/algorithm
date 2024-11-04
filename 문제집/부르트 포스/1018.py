import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(n)]
    min_cnt = 64

    for i in range(n-7):
        for j in range(m-7):
            count_W = 0
            count_B = 0

            for x in range(8):
                for y in range(8):

                    if (x+y) % 2 == 0:
                        if board[i+x][j+y] == 'W':
                            count_W += 1
                        else:
                            count_B += 1
                    else:
                        if board[i+x][j+y] == 'B':
                            count_W += 1
                        else:
                            count_B += 1
            
            min_cnt = min(min_cnt, count_W, count_B)

    print(min_cnt)
    return

if __name__ == "__main__":
    main()