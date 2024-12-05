import sys

def calcul(a):
    global energy
    if len(ball)==2:
        if a > energy:
            energy = a
        return
    else:
        for i in range(1, len(ball)-1):
            temp = ball[i-1]*ball[i+1]
            node = ball[i]
            del ball[i]
            calcul(a+temp)
            ball.insert(i, node)

n = int(sys.stdin.readline())
ball = list(map(int, sys.stdin.readline().split()))
energy = 0

calcul(0)
print(energy)