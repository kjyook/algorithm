import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    input_list = [sys.stdin.readline().strip() for _ in range(n)]
    int_dict, stirng_dict = {str(i+1): string for i, string in enumerate(input_list)}, {string: (i+1) for i, string in enumerate(input_list)}

    question = [sys.stdin.readline().strip() for _ in range(m)]

    for i in question:
        if i in int_dict:
            print(int_dict[i])
        elif i in stirng_dict:
            print(stirng_dict[i])

    return

if __name__ == "__main__":
    main()