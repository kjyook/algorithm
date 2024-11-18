import sys
input = sys.stdin.readline

def recursion(st):
    size = len(st)
    if size == 3:
        st[1][1] = " "
        return st
    
    answer = [["" for _ in range(size)] for _ in range(size)]

    for i in range(3):
        col = []
        row = []
        for j in range(3):
            if i == 1 and j == 1:
                row = [[" " for _ in range(size// 3)] for _ in range(len(st) // 3)]
            elif i == 2 and j == 2:
                row = recursion(st[size // 3 * i : size][size // 3 * j : size])
            elif i == 2:
                row = recursion(st[size // 3 * i : size][size // 3 * j : size // 3 * (j + 1)])
            elif j == 2:
                row = recursion(st[size // 3 * i : size // 3 * (i + 1)][size // 3 * j : size])
            else:
                row = recursion(st[size // 3 * i : size // 3 * (i + 1)][size // 3 * j : size // 3 * (j + 1)])


            if not col:
                col = row
            else:
                col = [x + y for x, y in zip(col, row)]

        for ls in col:
            answer.append(ls)

    print("input", st, "output", answer)

    return answer

def main():
    n = int(input())
    star = [["*" for _ in range(n)] for _ in range(n)]

    for row in recursion(star):
        print(''.join(map(str,row)))
    return

if __name__ == "__main__":
    main()