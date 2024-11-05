import sys

def main():
    n = int(sys.stdin.readline())

    dot_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dot_list.sort()
    
    for i in dot_list:
        print(' '.join(list(map(str,i))))
    
    return

if __name__ == "__main__":
    main()