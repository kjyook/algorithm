import sys

def main():
    n = int(sys.stdin.readline())
    stack = []

    for _ in range(n):
        num = list(map(int, sys.stdin.readline().split()))

        if num[0] == 1:
            stack.append(num[1])
        elif num[0] == 2:
            if len(stack) >= 1:
                print(stack[-1])
                stack.pop()
            else:
                print(-1)
        elif num[0] == 3:
            print(len(stack))
        elif num[0] == 4:
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif num[0] == 5:
            if len(stack) >= 1:
                print(stack[-1])
            else:
                print(-1)


    return

if __name__ == "__main__":
    main()