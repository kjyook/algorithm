import sys

def main():
    N,M = map(int, sys.stdin.readline().split())
    dot = [[0,0] for _ in range(M)]

    for i in range(M):
        dot[i][0], dot[i][1] = map(int,sys.stdin.readline().split())

    def dotLocation(a,b,c):
        temp = (b[1] - a[1])*(c[0] - b[0]) - (b[0] - a[0])*(c[1] - b[1])

        if temp==0:
            return 0
        elif temp>0:
            return 1
        else:
            return -1
        
    def border(dots):
        number = len(dots)
        if number<3:
            return []
        
        tempList=[]
        length=0
        for i in range(1,number):
            if dots[i][0] < dots[length][0]:
                length=i
            elif dots[i][0] == dots[length][0] and dots[i][1] < dots[length][1]:
                length=i

        p=length
        q=0

        while True:
            tempList.append(dots[p])
            q=(p+1)%number
            for i in range(number):
                if dotLocation(dots[p],dots[i],dots[q]) == -1:
                    q=i

            p=q
            if p==length:
                break

        return tempList

    tmp = border(dot)
    whiteDot = len(tmp)
    blueDot = M - whiteDot

    print(blueDot)

    return

if __name__=="__main__":
    main()