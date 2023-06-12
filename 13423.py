import sys

def calcul():
    a = int(sys.stdin.readline())
    dot = list(map(int, sys.stdin.readline().split()))
    count = 0

    for i in range(a):
        for j in range(i + 1, a):
            for k in range(j + 1, a):
                a1 = abs(dot[k] - dot[j])
                a2 = abs(dot[k] - dot[i])
                a3 = abs(dot[i] - dot[j])
                if a1 != a2 and  a2 != a3 and a3 != a1:
                    temp = 1
                else:
                    count += 1

    print(count)

    return

def main():
    N = int(sys.stdin.readline())
    
    for i in range(N):
        calcul()

    return

if __name__ == "__main__":
    main()