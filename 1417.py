import sys

def main():
    N = int(sys.stdin.readline())
    vote = []

    if N == 1:
        print(0)
        return

    for _ in range(N):
        vote.append(int(sys.stdin.readline()))

    count = 0

    while True:
        if max(vote) == vote[0]:
            temp = []
            for i in vote:
                temp.append(i)
            temp.pop(0)
            if max(temp) == vote[0]:
                print(count + 1)
                return
            else:
                print(count)
                return
        
        vote[vote.index(max(vote))] -= 1
        vote[0] += 1
        count += 1

if __name__ == "__main__":
    main()