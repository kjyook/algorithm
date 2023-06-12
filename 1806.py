import sys

def main():
    n, s = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))

    answer = 100001
    start = 0
    end = 0
    sum = num[0]

    while True:
        if sum >= s:
            answer = min(answer, end - start + 1)
            sum -= num[start]
            start += 1
        else:
            end += 1
            if end == n:
                break
            sum += num[end]

    if answer == 100001:
        print(0)
    else:
        print(answer)

    return

if __name__=="__main__":
    main()