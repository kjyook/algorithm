import sys

def main():
    n = int(sys.stdin.readline())
    queue = []
    front, rear = 0, 0

    for _ in range(n):
        command = list(sys.stdin.readline().split())

        if command[0] == "push":
            queue.append(int(command[1]))
            rear += 1
        elif command[0] == "pop":
            if rear - front == 0:
                print(-1)
            else:
                print(queue[front])
                front += 1
        elif command[0] == "size":
            print(rear - front)
        elif command[0] == "empty":
            if rear - front == 0:
                print(1)
            else:
                print(0)
        elif command[0] == "front":
            if rear - front == 0:
                print(-1)
            else:
                print(queue[front])
        elif command[0] == "back":
            if rear - front == 0:
                print(-1)
            else:
                print(queue[rear - 1])

    return

if __name__ == "__main__":
    main()