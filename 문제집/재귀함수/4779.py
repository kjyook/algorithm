import sys
input = sys.stdin.readline

def cantor(a):
    a = len(a)
    if a == 1:
        return "-"
    
    return cantor("-" * (a // 3)) + (" " * (a // 3)) + cantor("-" * (a // 3))

def main():
    while True:
        try:
            num = int(input())
            print(cantor("-" * (3 ** num)))
        except:
            break

    
    return

if __name__ == "__main__":
    main()