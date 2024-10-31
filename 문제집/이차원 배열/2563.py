import sys

def main():
    n = int(sys.stdin.readline())
    drawingPaper = [[0 for _ in range(100)] for _ in range(100)]

    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())

        for i in range(y, y+10):
            for j in range(x, x+10):
                drawingPaper[i][j] = 1

    count = 0
    for i in range(100):
        count += drawingPaper[i].count(1)

    print(count)

if __name__ == "__main__":
    main()