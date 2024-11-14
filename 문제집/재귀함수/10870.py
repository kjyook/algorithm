import sys

def pibo(a):
    if a == 1:
        return 1
    if a == 0:
        return 0
    
    return pibo(a - 1) + pibo(a - 2)

def main():
    n = int(sys.stdin.readline())
    print(pibo(n))
    return

if __name__ == "__main__":
    main()