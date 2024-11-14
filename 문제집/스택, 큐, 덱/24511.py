import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    c = list(map(int, sys.stdin.readline().split()))

    answer = []
    temp = []
    index = n - 1

    for i in reversed(a):
        if i == 0:
            temp.append(b[index])

        index -= 1

    temp = temp + c

    for i in temp:
        answer.append(str(i))

        if len(answer) == m:
            break
    
    print(' '.join(answer))

    return

if __name__ == "__main__":
    main()