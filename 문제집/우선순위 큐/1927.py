import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]
min_heap = [0]

def insert(a):
    min_heap.append(a)
    t = len(min_heap) - 1

    while t != 1:
        if min_heap[t // 2] > min_heap[t]:
            min_heap[t // 2], min_heap[t] = min_heap[t], min_heap[t // 2]
            t = t // 2
        else:
            break

    return

def remove():
    if len(min_heap) == 1:
        print(0)
        return
    
    print(min_heap[1])

    min_heap[1] = min_heap[-1]
    min_heap.pop()
    l = len(min_heap) - 1
    a = 1

    while a <= l:
        if 2*a > l:
            break
        if 2*a == l:
            if min_heap[2*a] < min_heap[a]:
                min_heap[2*a], min_heap[a] = min_heap[a], min_heap[2*a]
            break

        if min_heap[a] < min(min_heap[2*a], min_heap[2*a + 1]):
            break
        else:
            if min_heap[2*a] < min_heap[2*a + 1]:
                min_heap[2*a], min_heap[a] = min_heap[a], min_heap[2*a]
                a = 2 * a
            else:
                min_heap[2*a + 1], min_heap[a] = min_heap[a], min_heap[2*a + 1]
                a = 2 * a + 1

    return

for i in array:
    if i == 0:
        remove()
    else:
        insert(i)