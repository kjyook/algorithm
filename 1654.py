import sys

def main():
    k, n = map(int, sys.stdin.readline().split())
    line = []
    for _ in range(k):
        line.append(int(sys.stdin.readline()))

    left = 1
    right = max(line)
    temp = (left + right) // 2

    while left <= right:
        temp = (left + right) // 2
        answer = 0

        for i in line:
            answer += i //temp

        if answer >= n :
            left = temp + 1
        else:
            right = temp -1

    print(right)


if __name__ == "__main__":
    main()