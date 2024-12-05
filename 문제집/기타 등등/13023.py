import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    friend = [[] for _ in range(N)]
    visited = [0 for _ in range(N)]

    for _ in range(M):
        temp = list(map(int, sys.stdin.readline().split()))
        friend[temp[0]].append(temp[1])
        friend[temp[1]].append(temp[0])

    def dfs(people, count):
        if count==4:
            print(1); exit()
        for i in friend[people]:
            if visited[i] == 0:
                visited[i] = 1
                dfs(i, count+1)
                visited[i] = 0

    for i in range(N):
        visited[i] = 1
        dfs(i,0)
        visited[i] = 0
    
    print(0)

if __name__=="__main__":
    main()