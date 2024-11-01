import sys

def main():
    a, b, c, d, e, f = map(int, sys.stdin.readline().split())

    for x in range(-999, 1000):
        y = - a * x / b + c / b

        if d * x + e * y == f:
            print(x, int(y))
            break
    

if __name__ == "__main__":
    main()