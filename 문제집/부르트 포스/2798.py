import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    cards = list(map(int, sys.stdin.readline().split()))

    result = []

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                sum = cards[i] + cards[j] + cards[k]
                if sum < M:
                    result.append(sum)
                elif sum == M:
                    print(sum)
                    return
                else:
                    continue

    print(max(result))

if __name__ == "__main__":
    main()