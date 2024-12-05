import sys

def main():
    n, k, b = map(int, sys.stdin.readline().split())

    light = [0]*n

    for _ in range(b):
        a = int(sys.stdin.readline())
        light[a-1] = 1


    start = 0
    end = k
    temp = 0
    for i in range(k):
        temp += light[i]
    answer = temp 

    while True:
        if end == n:
            break

        temp = temp - light[start] + light[end]
        start += 1
        end += 1

        answer = min(temp, answer)

    print(answer)
    return

if __name__=="__main__":
    main()