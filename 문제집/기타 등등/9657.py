import sys

def main():
    n = int(sys.stdin.readline())
    game = ["SK","CY","SK","SK"]

    if n>4:
        for i in range(4,n):
            if game[i-1] == "CY" or game[i-3] == "CY" or game[i-4] == "CY":
                game.append("SK")
            else:
                game.append("CY")
                
    print(game[n-1])

if __name__ == "__main__":
    main()