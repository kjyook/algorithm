import sys

def main():
    stack = []
    n = int(input())
    for i in range(n):
        string = sys.stdin.readline()

        if "push" in string:
            stack.append(int(string.split()[1]))
        if "pop" in string:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[len(stack) - 1])
                del stack[len(stack) - 1]
        if "size" in string:
            print(len(stack))
        if "empty" in string:
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        if "top" in string:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[len(stack) - 1])


if __name__ == "__main__":
    main()