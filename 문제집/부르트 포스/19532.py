import sys

def main():
    a, b, c, d, e, f = map(int, sys.stdin.readline().split())


    for x in range(-999, 1000):
        #b 로 나눌때 b가 0이면 오류가 생기는 듯 . 이거 생각해서 코드 수정하면 될듯 싶습니다.

        if b == 0:
            if a * x != c:
                continue
            else:
                y = f/e - d/e * x
        else:
            y = - a * x / b + c / b

        if d*x + e*y == f:
            print(x, int(y))
            break
    
    return

if __name__ == "__main__":
    main()