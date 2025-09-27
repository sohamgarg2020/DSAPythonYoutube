def quicksort(nums, start = 0, end = None):
    if end is None:
        end = len(nums)-1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums


def partition(nums, start, end):
    left, right = start, end-1

    while right > left:
        if nums[left] <= nums[end]:
            left+= 1
        elif nums[right] > nums[end]:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]

    if nums[left] > nums[end]:
        nums[left], nums[end] = nums[end], nums[left]
        return left
    else:
        return end


list1 = [1, 5, 6, 2, 0, 11, 3]
print(quicksort(list1))