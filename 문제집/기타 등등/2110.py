import sys

def main():
    n, m = map(int, sys.stdin.readline().split())

    wifi = []
    for _ in range(n):
        wifi.append(int(sys.stdin.readline()))

    wifi.sort()
    left, right = 1, wifi[-1] - wifi[0]
    mid = 0
    result = 0


    if n == 2:
        print(wifi[n-1] - wifi[0])
    while left<=right:
        mid = (left+right)//2
        count = 1
        temp = wifi[0]

        for i in wifi:
            if i - temp >= mid:
                count += 1
                temp = i

        if count >= m:
            result = mid
            left = mid + 1
        elif count < m:
            right = mid - 1

    print(result)

    return

if __name__=="__main__":
    main()