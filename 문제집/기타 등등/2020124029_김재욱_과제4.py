import sys

#이 문제에 대한 풀이로 제가 작성한 블로그를 첨부합니다. https://kjyook.tistory.com/9

def main():
    N,M = map(int, sys.stdin.readline().split())
    score = [[0 for _ in range(N+1)] for _ in range(M+1)]
    honey = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    #왼쪽 밑의 점 중 지나가지 않는 점은 계산되지 않도록 지워준다
    for i in range(M):
        for j in range(i//2):
            honey[i][j] = 0

    #왼쪽 타일과 왼쪽 위 타일 중 최댓값과 해당 타일의 꿀 갯수를 더해 score에 저장한다.
    #y좌표가 홀수일 때와 y좌표가 짝수일 때 index관계가 다르므로 나눠서 계산하자.
    for i in range(1,M+1):
        for j in range(1,N+1):
            if i%2 == 1:
                score[i][j] = max(score[i][j-1], score[i-1][j-1]) + honey[i-1][j-1]
            else:
                score[i][j] = max(score[i][j-1], score[i-1][j]) + honey[i-1][j-1]

    print(score[M][N])

if __name__=="__main__":
    main()