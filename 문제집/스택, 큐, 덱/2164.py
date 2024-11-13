import sys

#원형 큐를 사용하여 해결함. 이게 한번에 카드 하나 날라가니까 while문이 n번 돌아가고. while문 안에서는 카드 이동(top과 bottom)이동이 3번 이뤄지는데 각각의 카드 이동의 시간복잡도는 1~n 사이이다. 최악의 경우에는 N^2의 시간복잡도를 보이겠지만 평균적으로는 nlogn의 시간복잡도를 보이지 않을까??
def main():
    n = int(sys.stdin.readline())
    card = [i + 1 for i in range(n)]
    top, bottom = 0, n - 1

    while True:
        if top == bottom:
            break

        card[top] = 0

        top = (top + 1) % n
        while not card[top]:
            top = (top + 1) % n
        
        top = (top + 1) % n
        while not card[top]:
            top = (top + 1) % n
    
        bottom = (bottom + 1) % n
        while not card[bottom]:
            bottom = (bottom + 1) % n
    
    print(card[top])

    return

if __name__ == "__main__":
    main()