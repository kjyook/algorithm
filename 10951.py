import sys

def main():
    while True:
        try:
            a,b = map(int, sys.stdin.readline().split())
            print(a+b)
        except:
            break
        
if __name__ == "__main__":
    main()