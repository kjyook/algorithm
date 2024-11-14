import sys

def increase_index(lst, idx, a):
    for _ in range(a):
        idx = (idx + 1) % len(lst)
        while not lst[idx]:
            idx = (idx + 1) % len(lst)

    return idx

def main():
    n, k = map(int, sys.stdin.readline().split())

    circle = [i + 1 for i in range(n)]
    answer = []
    index = -1

    for _ in range(n):
        index = increase_index(circle, index, k)
        answer.append(str(circle[index]))
        circle[index] = 0

    print("<"+', '.join(answer)+">")        

    return

if __name__ == "__main__":
    main()