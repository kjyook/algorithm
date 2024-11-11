import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    #중복도 허용될 필요 없고, 순서 안중요하고, 빨리 찾아야 하는경우. 그냥 set이 최고다.
    s = set()

    for _ in range(n):
        s.update([sys.stdin.readline().strip()])

    count = 0

    for _ in range(m):
        test = sys.stdin.readline().strip()
        if test in s:
            count += 1

    print(count)
    return

if __name__ == "__main__":
    main()