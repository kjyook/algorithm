import sys
input = sys.stdin.readline

n,m = map(int,input().split())
bridges = []
temp = []
ans = [i+1 for i in range(n)]
sum = 0

for _ in range(m):
    u,v,w = map(int,input().split())
    bridges.append([u,v,w])
    sum += w
print(bridges)
print("ans는 이렇게입니다",ans)
    
temp.append(1)
node = 1
cnt = 0
    
while True:
    mx,mnode = 0,0
    for bridge in bridges:
        print("let's go",bridge,temp)
        if bridge[0] in temp and bridge[1] not in temp and mx < bridge[2]:
            print("wow first case",bridge)
            mx = bridge[2]
            mnode = bridge[1]
        elif bridge[0] not in temp and bridge[1] in temp and mx < bridge[2]:
            print("wow second case", bridge)
            mx = bridge[2]
            mnode = bridge[0]
    
    if mnode != 0:
        cnt += mx
        node = mnode
        temp.append(node)
        print(temp)
    
    if len(temp) == n:
        print(sum-cnt)
        break