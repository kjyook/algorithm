import sys


def main():
    n = int(sys.stdin.readline())
    box = list(map(int, sys.stdin.readline().split()))

    answer = []

    for _ in range(n):
        answer.append(1)

    for i in range(n):
        temp = [0]
        for j in range(i):
            if box[j] < box[i]:
                temp.append(answer[j])

        answer[i] += max(temp)

    print(max(answer))

if __name__ == "__main__":
    main()