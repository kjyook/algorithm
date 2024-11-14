import sys

def pibo(a):
    if a == 0:
        return 1
    
    return a * pibo(a - 1)

def main():
    n = int(sys.stdin.readline())

    print(pibo(n))
    return

if __name__ == "__main__":
    main()