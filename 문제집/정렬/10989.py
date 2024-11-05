import sys

def main():
    n = int(sys.stdin.readline().strip())

    #메모리가 작으니 10000000가 될수있는 배열이 아닌 10000로 줄여서 해보자
    numbers = [0] * 10001
    
    for _ in range(n):
        numbers[int(sys.stdin.readline().strip())] += 1

    for i in range(10001):
        if numbers[i] != 0:
            for _ in range(numbers[i]):
                print(i)

    return

if __name__ == "__main__":
    main()