import sys
input = sys.stdin.readline

answer = []

#from -> 어디서왔니 to -> 어디로(n개를 보낸다) aux-> 남는 보조 폴폴
def hanoi(n, from_pole, to_pole, aux_pole):
    if n == 1:
        answer.append([from_pole, to_pole])
        return

    hanoi(n-1, from_pole, aux_pole, to_pole)
    answer.append([from_pole, to_pole])
    hanoi(n-1, aux_pole, to_pole, from_pole)

    return

def main():
    n = int(input())
    hanoi(n,1,3,2)

    print(len(answer))
    for i in answer:
        print(' '.join(map(str, i)))

    return

if __name__ == "__main__":
    main()