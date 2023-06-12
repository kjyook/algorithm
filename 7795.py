import sys

def main():
    n = int(sys.stdin.readline())

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        list_a = list(map(int, sys.stdin.readline().split()))
        list_b = list(map(int, sys.stdin.readline().split()))

        list_a.sort()
        list_b.sort()

        temp = 0
        count = 0

        for i in range(a):
            while True:
                if count == b or list_a[i] <= list_b[count]:
                    temp += count
                    break
                else:
                    count += 1  

        print(temp)
    return

if __name__ == "__main__":
    main()