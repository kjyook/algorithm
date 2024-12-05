import sys

def main():
    n = int(sys.stdin.readline())
    stack = []

    for i in range(n):
        a = int(sys.stdin.readline())
        
        if a == 0:
            del stack[len(stack) - 1]

        else:
            stack.append(a)

    print(sum(stack))

if __name__ == "__main__":
    main()