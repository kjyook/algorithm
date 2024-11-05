import sys

#직접 퀵정렬을 구현하여 풀이해보고 싶었다..!
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, larger_arr = [], [], []

    for word in arr:
        #길이가 차이나는 경우 길이가 가장 우선시 되는 배열
        if len(word) < len(pivot):
            lesser_arr.append(word)
        elif len(word) > len(pivot):
            larger_arr.append(word)
        #길이가 같은 경우 문자열의 순서를 비교하여 결정
        else:
            if word < pivot:
                lesser_arr.append(word)
            elif word > pivot:
                larger_arr.append(word)
    
    equal_arr.append(pivot)

    return quick_sort(lesser_arr) + equal_arr + quick_sort(larger_arr)

def main():
    n = int(sys.stdin.readline())

    str_list = [sys.stdin.readline().strip() for _ in range(n)]
    
    for i in quick_sort(str_list):
        print(i)

    return

if __name__ == "__main__":
    main()