import sys

def main():
    n = int(sys.stdin.readline())

    count = 0

    for i in range(n):
        s = sys.stdin.readline().strip()

        temp = []
        check = 0

        for index, j in enumerate(s):
            if j in temp:
                if s[index-1] != j:
                    check = 1
                    break
            else:
                temp.append(j)

        if check == 0:
            count += 1

    print(count)

if __name__ == "__main__":
    main()