import sys

def main():
    n,m = map(int, sys.stdin.readline().split())
    city = [[] for _ in range(n+1)]
    canGo = []
    visitied = [0]*(n+1)
    originalEdge = 0
    newEdge = 0
    

    #city라는 이차원 리스트는 city[i]에는 i와 연결된 엣지들의 정보가 [노드, 가중치] 형식으로 저장됩니다.
    for _ in range(m):
        a,b,c = map(int, sys.stdin.readline().split())
        city[a].append([b,c])
        city[b].append([a,c])

        #originalEdge는 총 edge들의 총합을 기록할 것입니다. 이 후 선택된 edge들과의 차이를 통해 버려진 edge를 파악하기 위함입니다.
        originalEdge += c


    #노드들은 1~n 이고 모든 노드들은 연결되어야 하므로 어디서 시작하는지 중요하지 않기에 그냥 1부터 하였습니다.
    #visited[i] 가 1 이면 나는 i에 방문한 것이고, 0이면 아직 방문하지 않은겁니다.
    #최소신장트리를 구하여 하므로 i가 0이면 가야하는 노드, 1이면 가지 않아도 되는 노드입니다
    visitied[1] = 1
    canGo = canGo + city[1]


    #최소신장트리를 만들때까지 작업을 수행합니다.
    while True:
        #보통의 최소신장트리와 다르게 가중치들은 최댓값들을 택해야 하므로 가중치중 최댓값을 찾습니다.
        max = 0
        temp = 0

        for i in canGo:
            #선택할 수 있는 노드들 중 가야하는 노드이면서 가중치가 가장 큰 노드를 찾습니다.
            if max < i[1] and visitied[i[0]] == 0:
                max = i[1]
                temp = i

        #가야하는 노드인 temp를 찾지 못했다면 모두 연결이 된 상태입니다.
        if temp == 0:
            #모든 엣지의 가중치 총합에서 선택된 엣지의 가중치를 빼서 제거된 엣지의 가중치를 구합니다.
            print(originalEdge-newEdge)
            return
        else:
            #가야하는 노드인 temp를 골랐으니 visitied에 기록하고, newEdge에도 가중치를 더해줍니다.
            visitied[temp[0]] = 1
            newEdge += temp[1]

            #이미 간 노드와 연결된 엣지는 삭제
            for j in canGo:
                if visitied[j[0]] == 1:
                    canGo.remove(j)
            
            #새롭게 갈 수 있는 노드와 연결된 엣지를 추가
            for j in city[temp[0]]:
                if visitied[j[0]] == 0:
                    canGo.append(j)

                

if __name__=="__main__":
    main()