import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]
max_heap = [0]

def insert(a):
    max_heap.append(a)
    t = len(max_heap) - 1

    while t != 1:
        if max_heap[t // 2] < max_heap[t]:
            max_heap[t // 2], max_heap[t] = max_heap[t], max_heap[t // 2]
            t = t // 2
        else:
            break

    return

def remove():
    if len(max_heap) == 1:
        print(0)
        return
    
    print(max_heap[1])

    max_heap[1] = max_heap[-1]
    max_heap.pop()
    l = len(max_heap) - 1
    a = 1

    while a <= l:
        if 2*a > l:
            break
        if 2*a == l:
            if max_heap[2*a] > max_heap[a]:
                max_heap[2*a], max_heap[a] = max_heap[a], max_heap[2*a]
            break

        if max_heap[a] > max(max_heap[2*a], max_heap[2*a + 1]):
            break
        else:
            if max_heap[2*a] > max_heap[2*a + 1]:
                max_heap[2*a], max_heap[a] = max_heap[a], max_heap[2*a]
                a = 2 * a
            else:
                max_heap[2*a + 1], max_heap[a] = max_heap[a], max_heap[2*a + 1]
                a = 2 * a + 1

    return

for i in array:
    if i == 0:
        remove()
    else:
        insert(i)