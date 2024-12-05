import sys

def main():
    n = int(sys.stdin.readline())
    num_list = []
    answer = []
    number = 0
    temp = True

    for i in range(n):
        a = int(sys.stdin.readline())

        while True:
            if a > number:
                number += 1
                num_list.append(number)
                answer.append("+")
            else:
                if num_list[len(num_list) - 1] == a:
                    del num_list[len(num_list) - 1]
                    answer.append("-")
                    break
                else:
                    temp = False
                    break
    
    if temp == True:
        print(*answer, sep='\n')
    else:
        print("NO")

if __name__ == "__main__":
    main()