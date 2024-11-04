import sys

def main():
    n = int(sys.stdin.readline())

    count_movie = 0
    i = 666

    while True:
        if '666' in str(i):
            count_movie += 1
            
        if count_movie == n:
            print(i)
            break

        if count_movie > 10000:
            print("10000이하의 수를 입력해주세요")
            break

        i += 1

if __name__ == "__main__":
    main()