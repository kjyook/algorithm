import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
operator = list(map(int, input().split()))
oprt_list = []
answer = set()

def calulator():
    result = num_list[0]

    for index, symbol in enumerate(oprt_list):
        if symbol == 0:
            result += num_list[index + 1]
        elif symbol == 1:
            result -= num_list[index + 1]
        elif symbol == 2:
            result *= num_list[index + 1]
        else:
            result = int(result / num_list[index + 1])  #python의 음수나누기 결과값을 참조하여 //기호가 아닌 /후 int 함수를 활용
    
    answer.add(result)

    return

def backtracking(a):
    if a == n - 1:
        calulator()
        return

    for i in range(4):
        if operator[i]:
            oprt_list.append(i)
            operator[i] -= 1
            backtracking(a + 1)
            oprt_list.pop()
            operator[i] += 1
        
    return

backtracking(0)

print(int(max(answer)))
print(int(min(answer)))