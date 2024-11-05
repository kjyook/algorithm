import sys

def main():
    n = int(sys.stdin.readline().strip())

    numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]
    
    numbers.sort()

    for i in numbers:
        print(i)

    return

if __name__ == "__main__":
    main()