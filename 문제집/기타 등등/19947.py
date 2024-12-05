import sys

def main():
    H, Y = map(int, sys.stdin.readline().split())

    stock = [0 for i in range(Y + 1)]
    stock[0] = H

    for i in range(1, Y + 1):
        if i>=5:
            stock[i] = max(stock[i-1]*1.05, stock[i-3]*1.2, stock[i-5]*1.35)
        elif i>=3:
            stock[i] = max(stock[i-1]*1.05, stock[i-3]*1.2)
        else:
            stock[i] = stock[i-1]*1.05
        stock[i] = int(stock[i])

    print(stock[Y])

if __name__ == "__main__":
    main()