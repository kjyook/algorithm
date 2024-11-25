import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
max_int = -2000
record = 0

#리스트를 정방향으로 순회하면서 누적합을 구할것이다. 누적합은 구하면서 maxint보다 크다면 이를 maxint에 기록하고
#누적합이 음수가 된다는 것은 뒤의 것에 더해질때 도움이 안된다는 것이므로 누적합을 초기화하고 뒤로 나아가면 된다.
for i in num:
    record += i
    if record > max_int:
        max_int = record
    
    if record < 0:
        record = 0

print(max_int)