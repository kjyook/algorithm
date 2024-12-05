import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    num = [[0 for j in range(N+1)] for i in range(N+1)]

    for i in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            num[i+1][j+1] = temp[j] + num[i+1][j]
        
        for j in range(N):
            num[i+1][j+1] += num[i][j+1]
            
    for _ in range(M):
        a,b,c,d = map(int, sys.stdin.readline().split())
        print(num[c][d] -num[c][b-1] -num[a-1][d] +num[a-1][b-1])

if __name__ == "__main__":
    main()