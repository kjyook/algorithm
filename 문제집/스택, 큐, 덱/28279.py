import sys

def main():
    n = int(sys.stdin.readline())
    deque = [0 for _ in range(n)]
    front, rear = 0, 0

    for _ in range(n):
        command = list(sys.stdin.readline().split())

        if command[0] == '1':
            front = (front + n - 1) % n
            deque[front] = int(command[1])
        elif command[0] == '2':
            deque[rear] = int(command[1])
            rear = (rear + 1) % n
        elif command[0] == '3':
            if front == rear:
                print(-1)
            else:
                print(deque[front])
                deque[front] = 0
                front = (front + 1) % n
        elif command[0] == '4':
            if front == rear:
                print(-1)
            else:
                rear = (rear + n - 1) % n
                print(deque[rear])
                deque[rear] = 0
        #원래 이 부분만 복잡도가 O(n)이여서 시간초과였는데 1로 바꾸니까 해결되네...? ㅠ_ㅠ
        elif command[0] == '5':
            if rear >= front:
                print(rear - front)
            else:
                print(rear + n - front)
        elif command[0] == '6':
            if front == rear:
                print(1)
            else:
                print(0)
        elif command[0] == '7':
            if front == rear:
                print(-1)
            else:
                print(deque[front])
        elif command[0] == '8':
            if front == rear:
                print(-1)
            else:
                print(deque[(rear + n - 1) % n])

    return

if __name__ == "__main__":
    main()