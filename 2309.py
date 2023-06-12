import sys

def main():

    a = []

    for i in range(9):
        a.append(int(sys.stdin.readline()))

    find = sum(a) - 100

    for i in range(9):
        for j in range(i + 1,9):
            if a[i] + a[j] == find:
                del a[j]
                del a[i]
                a.sort()
                for k in a:
                    print(k)

                return
            
if __name__ == "__main__":
    main()