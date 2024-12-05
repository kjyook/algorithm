import sys

def main():
    while True:
        a,b = map(int, sys.stdin.readline().split())
        if a == b == 0:
            break
        else:
            print(a+b)

if __name__ == "__main__":
    main()