import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    A, B = set(), set()
    al = list(map(int, sys.stdin.readline().split()))
    bl = list(map(int, sys.stdin.readline().split()))

    for i in al:
        A.add(i)
    for i in bl:
        B.add(i)

    count = 0

    for i in A:
        if i in B:
            count += 1

    print(len(A) + len(B) - count * 2)

    return

if __name__ == "__main__":
    main()