import sys

def main():
    N = int(sys.stdin.readline())
    M = map(int, sys.stdin.readline())

    A = list(map(int, sys.stdin.readline().split()))

    count = abs(100 - N)

    for i in range(1000001):
        number = str(i)
        for j in range(len(number)):
            if int(number[j]) in A:
                break
            elif j == len(number) -1:
                count = min(count, abs(i - N) + len(number))

    print(count)



if __name__ == "__main__":
    main()