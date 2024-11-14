import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    c = list(map(int, sys.stdin.readline().split()))

    answer = []
    temp = []
    index = n - 1


    #스택일때는 사실 들어간거 그대로 나오니 계산 x, 큐일때는 앞에 하나씩 붙는거다.
    #사실 나도 컴퓨터처럼 흐름따라서 풀었더니 시간복잡도가 n*m 이 나오더라. 흐름따라 풀면 다 맞을수는 있지만 시간초과가 나오기도 한다. 과정들을 쪼개서 간소화할 수 있는 부분을 찾아보자
    for i in reversed(a):
        if i == 0:
            temp.append(b[index])

        index -= 1

    temp = temp + c

    for i in temp:
        answer.append(str(i))

        if len(answer) == m:
            break
    
    print(' '.join(answer))

    return

if __name__ == "__main__":
    main()