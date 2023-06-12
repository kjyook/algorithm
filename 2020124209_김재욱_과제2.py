import sys

def main():
    a,b,n = map(int, sys.stdin.readline().split())
    count = 0

    def gcb(x, y):
        tma = x
        tmb = y

        while True:
            r = tma%tmb
            if r==0:
                break
            tma=tmb
            tmb=r

        if tmb == 1:
            return 1
        else:
            return 0
        
    for i in range (a, b+1):
        count += gcb(i,n)
        
    return  print(count)

if __name__=="__main__":
    main()