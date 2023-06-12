import sys
input = sys.stdin.readline()

n, m, k = map(int, input().split())
beer = []

for _ in range(k):
    beer.append(list(map(int, input().split())))