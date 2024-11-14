import sys

def main():
    n = int(sys.stdin.readline())
    balloons = list(map(int, sys.stdin.readline().split()))
    index = 0
    answer = []

    def idx_move(idx, a):
        if a > 0:
            for _ in range(a):
                idx = (idx + 1) % n
                while not balloons[idx]:
                    idx = (idx + 1) % n
        else:
            for _ in range(-a):
                idx = (idx + n - 1) % n
                while not balloons[idx]:
                    idx = (idx + n - 1) % n
        return idx
    
    for i in range(n):
        answer.append(str(index + 1))
        temp = balloons[index]
        balloons[index] = 0

        if i == n - 1:
            break
        
        index = idx_move(index, temp)

    print(' '.join(answer))
    return

if __name__ == "__main__":
    main()