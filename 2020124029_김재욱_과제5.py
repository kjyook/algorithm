import sys

#https://kjyook.tistory.com/14 이 문제에 대한 풀이를 작성한 블로그를 첨부합니다.
def main():
    a,b,c,d,r = map(int,sys.stdin.readline().split())
    left = max(a,c)
    right = min(a+r,c+r)
    bottom = max(b-r,d-r)
    top = min(b,d)
    
    #입력받은 값이 주어진 갑의 범위가 맞는지 확인
    if a<0 or b<0 or c<0 or d<0 or r<0 or a>1000000 or b>1000000 or c>1000000 or d>1000000 or r>500000:
        print("잘못된 입력입니다.")
        return

    if left>=right or bottom>=top:
        print(r*r*2)
    else:
        print(r*r*2 - (right - left)*(top - bottom))

if __name__=="__main__":
    main()