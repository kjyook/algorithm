import sys
input = sys.stdin.readline

n = int(input())
price = [list(map(int, input().split())) for _ in range(n) ]

#이거 백트래킹 쓰면 time limit터질려나
#안해봤는데 터질듯 하니 list[3]짜리에 지금까지의 최소를 담아와서 누적시키는 방법으로 해보자
record_min = [0] * 3

for i in price:
    temp = [i for i in record_min]
    idx = temp.index(min(temp))

    if idx == 0:
        record_min[1] = temp[0] + i[1]
        record_min[2] = temp[0] + i[2]
        if temp[1] < temp[2]:
            record_min[0] = temp[1] + i[0]
        else:
            record_min[0] = temp[2] + i[0]
    elif idx == 1:
        record_min[0] = temp[1] + i[0]
        record_min[2] = temp[1] + i[2]
        if temp[0] < temp[2]:
            record_min[1] = temp[0] + i[1]
        else:
            record_min[1] = temp[2] + i[1]
    else:
        record_min[0] = temp[2] + i[0]
        record_min[1] = temp[2] + i[1]
        if temp[0] < temp[1]:
            record_min[2] = temp[0] + i[2]
        else:
            record_min[2] = temp[1] + i[2]

print(min(record_min))