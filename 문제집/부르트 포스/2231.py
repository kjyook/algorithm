import sys

def main():
    n = int(sys.stdin.readline())

    for i in range(1, n+1):
        sum = i
        for j in str(i):
            sum += int(j)

        if sum == n:
            print(i)
            return
    
    print(0)


if __name__ == "__main__":
    main()