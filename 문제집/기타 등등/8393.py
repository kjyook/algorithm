def main():
    n = int(input())
    sum = 0
    for i in range(n):
        sum += n
        n -= 1
    print(sum)

if __name__ == "__main__":
    main()
    