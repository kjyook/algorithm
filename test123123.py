def orientation(p, q, r):
    # 세 점 p, q, r의 방향을 반환하는 함수
    # 양수: 반시계 방향, 음수: 시계 방향, 0: 일직선
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return -1

def convex_hull(points):
    n = len(points)
    if n < 3:
        return []

    hull = []
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
        elif points[i][0] == points[l][0] and points[i][1] < points[l][1]:
            l = i

    p = l
    q = 0
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == -1:
                q = i
        p = q
        if p == l:
            break

    return hull

# 입력 받기
N, M = map(int, input().split())
points = []
for _ in range(M):
    x, y = map(int, input().split())
    points.append((x, y))

# 볼록 껍질 구하기
hull = convex_hull(points)

# 볼록 껍질 내부에 있는 하얀 점의 개수
white_inside_hull = len(hull)

# 파란 점의 개수
blue_points = M - white_inside_hull

# 결과 출력
print(blue_points)
