import sys

def main():
    m, seed, x1, x2 = map(int, sys.stdin.readline().split())

    a = 0
    c = 0
    
    def dfs(num, a, c):
        return (a * num + c) % m

    def run():

        for i in range(0, m):
            a = i

            for j in range(0, m):
                c = j

                temp1 = dfs(seed, a, c)
                temp2 = dfs(temp1, a, c)

                if x1 == temp1 and x2 == temp2:
                    print(a, c)
                    return

    run()


if __name__ == "__main__":
    main()