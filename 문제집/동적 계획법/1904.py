import sys
input = sys.stdin.readline

n = int(input())
answer = [0] * 1000001
answer[1] = 1
answer[2] = 2

#처음에는 탑다운 방식으로 풀었는데 그렇게 될경우 중복계산이 유발되고 시간복잡도가 2^n까지 올라가는것 같다.
#하지만 바텀업 방식은 n의 복잡도에서 해결된다. 내가 가진 힌트를 가지고 작은 단위부터 해결할 수 있는 법을 고려해보자
for i in range(3, n+1):
    answer[i] = (answer[i - 1] + answer[i - 2]) % 15746

print(answer[n])