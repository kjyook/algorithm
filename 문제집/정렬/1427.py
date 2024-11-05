import sys

def main():
    n = int(sys.stdin.readline())

    num_list = [int(a) for a in str(n)]
    num_list.sort(reverse=True)
    str_list = list(map(str, num_list))

    print(''.join(str_list))

    return

if __name__ == "__main__":
    main()