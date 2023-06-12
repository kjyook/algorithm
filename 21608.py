import sys

def main():
    n = int(sys.stdin.readline())

    students = []
    like = [[]] * (n*n)
    check = [0] * 10

    for i in range(n*n):
        temp = list(map(int, sys.stdin.readline().split()))
        students.append(temp[0])
        del temp[0]
        like[i].append(temp)
        for j in range(4):
            check[temp[i]] += 1

    seat = [[0 for _ in range(n)] for _ in range(n)]
    print(seat)
    

    return

if __name__=="__main__":
    main()