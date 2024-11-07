import sys

def main():
    n = int(sys.stdin.readline())
    a_list = list(map(int, sys.stdin.readline().split()))
    a_list = set(a_list)

    m = int(sys.stdin.readline())
    b_list = list(map(int, sys.stdin.readline().split()))
    
    answer = []

    for i in b_list:
        if i in a_list:
            answer.append('1')
        else:
            answer.append('0')

    print(' '.join(answer))

    return

if __name__ == "__main__":
    main()