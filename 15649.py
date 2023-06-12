import sys

def main():

    n, m= map(int, sys.stdin.readline().split())
    array = []

    def dfs():
        if len(array) == m:
            print(*array)
            return
        
        for i in range(1, n + 1):
            if i not in array:
                array.append(i)
                dfs()
                array.pop()

    dfs()
    


if __name__ == "__main__":
    main()