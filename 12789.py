import sys

def main():
    N = int(sys.stdin.readline())
    person = list(map(int, sys.stdin.readline().split()))
    temp = [1001 for _ in range(N)]

    while len(person) != 0:
        if person[0] == min(person) and min(person) < min(temp):
            person.pop(0)
        elif temp[-1] == min(temp) and min(person) > min(temp):
            temp.pop(-1)
        else:
            temp.append(person[0])
            person.pop(0)
    
    while len(temp) != N:
        if temp[-1] == min(temp):
            temp.pop(-1)
        else:
            return print("Sad")
    
    return print("Nice")


    return

if __name__ == "__main__":
    main()