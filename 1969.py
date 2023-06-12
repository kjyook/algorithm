import sys

def main():
    n, m = map(int, sys.stdin.readline().split())

    array = []
    answer = ""
    sum = 0

    for i in range(n):
        temp = sys.stdin.readline()
        array.append(temp)

    for i in range(0, m):
        dna = ['A','C','G','T']
        dna_list = [0, 0, 0, 0]

        for j in range(0, n):
            if array[j][i] == 'A':
                dna_list[0] += 1
            elif array[j][i] == 'C':
                dna_list[1] += 1
            elif array[j][i] == 'G':
                dna_list[2] += 1
            elif array[j][i] == 'T':
                dna_list[3] += 1

        temp = ''

        for j in range(0, 4):
            if dna_list[j] == max(dna_list):
                temp = j
                break
        
        answer += dna[j]
        sum += n - max(dna_list)
    
    print(answer)
    print(sum)

if __name__ == "__main__":
    main()