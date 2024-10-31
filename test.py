# prime_list는 1부터 10000사이의 소수가 오름차순으로 저장된 리스트예요.
from prime import prime_list

# 합계가 짝수가 되는 두 소수를 찾는 함수예요.
def goldbach(arr):
    # 합계가 짝수가 되는 두 소수를 작은 수부터 차례로 리스트에 저장해 주세요.
    num_list = []

    for number in arr:
        for i in prime_list:
            temp = number - i
            if temp in prime_list:
                num_list.append([i,temp])

    return None


arr = [int(x) for x in input().split()]

for i in goldbach(arr):
    print(i[0], i[1])
