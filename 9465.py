import sys

def main():
    
    def calcul():
    
        a = int(sys.stdin.readline())

        number = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

        if a > 1:
            number[0][1] += number[1][0]
            number[1][1] += number[0][0]

            for i in range(2, a):
                number[0][i] += max(number[1][i-1], number[1][i-2])
                number[1][i] += max(number[0][i-1], number[0][i-2])

            print(max(number[0][a-1], number[1][a-1]))
        else:
            print(max(number[0][0], number[1][0]))

    n = int(sys.stdin.readline())

    for _ in range(n):
        calcul()



if __name__ == "__main__":
    main()