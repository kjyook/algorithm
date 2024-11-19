import sys
input = sys.stdin.readline

def recursion(st):
    size = len(st)
    if size == 3:
        st[1][1] = " "
        return st
    
    answer = []

    for i in range(3):
        col = []
        row = []
        for j in range(3):
            if i == 1 and j == 1:
                row = [[" " for _ in range(size// 3)] for _ in range(len(st) // 3)]
            else:
                row = recursion([[st[a][b] for b in range(size // 3 * j, size // 3 * (j + 1))] for a in range(size // 3 * i, size // 3 * (i + 1))])
                #2d list slicing -> 불가능 그냥 for문 이용해서 하나씩 집어넣어주자...
                
            if not col:
                col = row
            else:
                col = [x + y for x, y in zip(col, row)]

        for ls in col:
            answer.append(ls)

    return answer

def main():
    n = int(input())
    star = [["*" for _ in range(n)] for _ in range(n)]

    for row in recursion(star):
        print(''.join(map(str,row)))
    return

if __name__ == "__main__":
    main()