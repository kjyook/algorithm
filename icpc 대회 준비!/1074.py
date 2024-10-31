import sys

def main():
    N, r, c = map(int, sys.stdin.readline().split())
    count = 0

    while N != 0:
        N -= 1

        if r < 2**N and c < 2**N:
            count += 0
        elif r >= 2**N and c < 2**N:
            count += 2**(2*N)*2
            r -= 2**N
        elif r < 2**N and c >= 2**N:
            count += 2**(2*N)
            c -= 2**N
        else:
            count += 2**(2*N)*3
            r -= 2**N
            c -= 2**N

    print(count)

if __name__ == "__main__":
    main()