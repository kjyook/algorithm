import sys

def main():
    N, M = map(int, sys.stdin.readline().split())

    circle = [i for i in range(1, N+1)]
    temp = []
    index = 0

    while len(circle) != 0:
        index = (index + M -1) % len(circle)
        temp.append(circle[index])
        circle.pop(index)

    print("<",end="")
    for i in range(N):
        if i != N-1:
            print(temp[i],end=", ")
        else:
            print(temp[i],end="")
    print(">")


if __name__ == "__main__":
    main()