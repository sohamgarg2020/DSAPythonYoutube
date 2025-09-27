def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2

    left = nums[:mid]
    right = nums[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(list1, list2):
    s_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            s_list.append(list1[i])
            i += 1
        else:
            s_list.append(list2[j])
            j += 1

    return s_list + list1[i:] + list2[j:]
