import sys

def main():
    n = int(sys.stdin.readline())

    for i in range(n):
        str = list(sys.stdin.readline().rstrip())
        check = 0

        for i in range(len(str)):
            if check == 0 and str[len(str) - 1] == '(':
                check = -1
                break
            elif str[len(str) - 1] == '(':
                check -= 1
                del str[len(str) - 1]
            elif str[len(str) - 1] == ')':
                check += 1
                del str[len(str) - 1]
        
        if check == 0:
            print("YES")
        else:
            print("NO")



if __name__ == "__main__":
    main()