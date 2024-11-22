import sys
input = sys.stdin.readline
num = [[[0] * (21) for _ in range(21) ] for i in range(21) ]

def dp(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    if x > 20 or y > 20 or z > 20:
        return dp(20, 20, 20)
    
    if num[x][y][z]:
        return num[x][y][z]
    
    if x < y < z:
        num[x][y][z] = dp(x, y, z - 1) + dp(x, y - 1, z - 1) - dp(x, y - 1, z)
    else:
        num[x][y][z] = dp(x - 1, y, z) + dp(x - 1, y - 1, z) + dp(x - 1, y, z - 1) - dp(x - 1, y - 1 , z - 1)

    return num[x][y][z]

def w(a, b, c):
    answer = dp(a, b, c)

    print(f"w({a}, {b}, {c}) = {answer}")
    return


while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break
    else:
        w(a, b, c)

