import sys

def main():
    n = int(sys.stdin.readline())

    member_list = []

    for _ in range(n):
        age, name = sys.stdin.readline().split()
        member_list.append([int(age), name])

    member_list.sort(key=lambda x:x[0])



    for i in member_list:
        k = [str(i[0]), i[1]]
        print(' '.join(k))

    return

if __name__ == "__main__":
    main()