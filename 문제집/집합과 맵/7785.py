import sys

def main():
    n = int(sys.stdin.readline())
    s = set()

    for _ in range(n):
        name, status = sys.stdin.readline().strip().split(' ')

        if status == 'enter':
            s.add(name)
        elif status == 'leave':
            s.remove(name)

    for i in sorted(s, reverse=True):
        print(i)

    return

if __name__ == "__main__":
    main()