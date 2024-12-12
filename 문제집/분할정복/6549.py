import sys
input = sys.stdin.readline

def largest_rec(a):
    def max_area(lst, start, last):
        if start == last:
            return lst[start]
        
        mid = (start + last) // 2

        left_area = max_area(lst, start, mid)
        right_area = max_area(lst, mid + 1, last)
        mid_area = find_middle_rec(lst, start, last, mid)

        return max(left_area, right_area, mid_area)

    def find_middle_rec(lst, start, last, mid):
        left = mid
        right = mid + 1
        min_height = min(lst[left], lst[right])
        max_rec = 2 * min_height

        while left > start or right < last:
            if right < last and (left == start or lst[left - 1] < lst[right + 1]):
                right += 1
                min_height = min(min_height, lst[right])
            else:
                left -= 1
                min_height = min(min_height, lst[left])

            max_rec = max(max_rec, min_height * (right - left + 1))

        return max_rec

    return max_area(a[1:], 0, a[0] - 1)

while True:
    box = list(map(int, input().split()))

    if box[0] == 0:
        break

    print(largest_rec(box))