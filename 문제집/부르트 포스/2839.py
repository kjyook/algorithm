import sys

def main():
    n = int(sys.stdin.readline())

    min_count = 0

    if n % 5 == 0:
        print(n//5)
        return
    
    for i in range(n//5, -1, -1):
        if not (n - 5*i) % 3 == 0:
            continue
        else:
            print(i + (n - 5*i) // 3)
            return
        
    print(-1)
    return

if __name__ == "__main__":
    main()