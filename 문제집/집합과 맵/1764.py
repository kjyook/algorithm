import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    
    people = set()
    count = 0
    answer = []
    
    for _ in range(n):
        people.add(sys.stdin.readline().strip())

    for _ in range(m):
        temp = sys.stdin.readline().strip()
        
        if temp in people:
            count += 1
            answer.append(temp)

    answer.sort()

    print(count)
    for i in answer:
        print(i)

    return

if __name__ == "__main__":
    main()