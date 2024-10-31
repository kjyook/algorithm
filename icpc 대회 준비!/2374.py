import sys

def main():
    n = int(sys.stdin.readline())
    number = [int(sys.stdin.readline()) for _ in range(n)]

    def removeOverrap(numlist):
        temp = [numlist[0]]
        for i in numlist:
            if not i in temp:
                temp.append(i)

        return temp
    
    def addNumber(a, numlist):
        numlist[a-1] += 1
        numlist = removeOverrap(numlist)

        return numlist
    
    number = removeOverrap(number)   

    count = 0
    while len(number)>1:
        number = addNumber(number.index(min(number)) + 1, number)
        count += 1

    print(count)


if __name__=="__main__":
    main()