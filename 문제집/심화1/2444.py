import sys

def main():
    n = int(sys.stdin.readline())

    for i in range(1, n+1):
        print(" "*(n-i) + "*"*(2*i-1))

    for i in range(n-1, 0, -1):
        print(" "*(n-i) + "*"*(2*i -1))

if __name__ == "__main__":
    main()