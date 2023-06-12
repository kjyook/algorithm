import sys

def main():
    n = int(input())
    count = 1
    for i in range(n):
        a,b = map(int, sys.stdin.readline().split())
        print(f'Case #{count}: {a} + {b} = {a+b}')
        count += 1

if __name__ == "__main__":
    main()