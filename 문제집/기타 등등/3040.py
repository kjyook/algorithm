import sys

def main():
    array = []
    sum = 0
    for i in range(9):
        a = int(sys.stdin.readline())
        array.append(a)
        sum += a
    
    a = 0
    b = 1
    for i in range(36):
        if sum - array[a] - array[b] == 100:
            del array[a]
            del array[b - 1]
            break

        b += 1
        if b == 9:
            a += 1
            b = a + 1

    print(*array,sep = '\n')


if __name__ == "__main__":
    main()