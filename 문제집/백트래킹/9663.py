import sys
input = sys.stdin.readline

n = int(input())
colums = [0 for _ in range(n)]
diagonals1 = set()
diagonals2 = set()
count = 0

def check(r):
    for row in range(r):
        if colums[r] == colums[row] or r - row == abs(colums[r] - colums[row]):
            return False
    return True

def queen(a):
    global count
    
    if a == n:
        count += 1
        return
    
    for i in range(1, n + 1):
        colums[a] = i
        if check(a):
            queen(a + 1)


queen(0)
print(count)