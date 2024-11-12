import sys

def main():
    word = sys.stdin.readline().strip()
    answer = set()

    for i in range(len(word)):
        for j in range(len(word)-i):
            if word[i:j+i+1] not in answer:
                answer.add(word[i:j+i+1])   
    
    print(len(answer))
    return

if __name__ == "__main__":
    main()