import sys

def main():
    n = int(sys.stdin.readline())
    a_list = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    b_list = list(map(int, sys.stdin.readline().split()))

    number_card = {}
    answer = []

    for i in a_list:
        if i in number_card:
            number_card[i] += 1
        else:
            number_card[i] = 1
    
    for i in b_list:
        if i in number_card:
            answer.append(str(number_card[i]))
        else:
            answer.append('0')

    
    print(' '.join(answer))

    return

if __name__ == "__main__":
    main()