import sys
from collections import deque

def main():
    def bfs(start):
        queue = deque()
        queue.append(start)
        while queue:
            start = queue.popleft()
            for n in family[start]:
                if checked[n] == 0:
                    checked[n] = checked[start] + 1
                    queue.append(n)
    
    n = int(sys.stdin.readline())
    target1, target2 = map(int,sys.stdin.readline().split())
    family = [[] for _ in range(n+1) ]
    checked = [0]*(n+1)

    for _ in range(int(sys.stdin.readline())):
        p, a = map(int, sys.stdin.readline().split())
        family[a].append(p)
        family[p].append(a)
    
    bfs(target1)
    print(checked[target2] if checked[target2]>0 else -1)

    
    return

if __name__=="__main__":
    main()