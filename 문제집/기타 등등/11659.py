import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    number = [0] + list(map(int, sys.stdin.readline().split()))

    temp = [0 for _ in range(n+1)]

    for k in range(1, n+1):
        temp[k] = temp[k-1] + number[k]

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        print(temp[j] - temp[i-1])


    return

if __name__=="__main__":
    main()