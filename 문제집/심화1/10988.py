import sys

def main():
    s = sys.stdin.readline().strip()

    for index, i in enumerate(s):
        if i != s[-(index+1)]:
            print(0)
            return
        
    print(1)

if __name__ == "__main__":
    main()