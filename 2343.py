import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    line = list(map(int, sys.stdin.readline().split()))

    left , right = max(line), sum(line)
    answer = (left + right) // 2

    while left <= right:
        answer = (left + right) // 2
        count, total = 1, 0
        
        for i in line:
            if i + total > answer:
                count += 1
                total = 0
            total += i

        if count <= m:
            right =  answer -1
        else:
            left = answer + 1

    print(left)

    return

if __name__=="__main__":
    main()