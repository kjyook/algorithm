import sys

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    lesser_list, equal_list, larger_list = [], [], []

    for i in arr:
        if i > pivot:
            larger_list.append(i)
        elif i < pivot:
            lesser_list.append(i)
        else:
            continue

    equal_list.append(pivot)

    return quick_sort(lesser_list) + equal_list + quick_sort(larger_list)


def main():
    n = int(sys.stdin.readline())

    dot_list = list(map(int, sys.stdin.readline().split()))
    sorted_list = quick_sort(dot_list)
    value_to_index = {value : idx for idx, value in enumerate(sorted_list)}
    answer_list = [str(value_to_index[i]) for i in dot_list]

    print(' '.join(answer_list))

    return

if __name__ == "__main__":
    main()