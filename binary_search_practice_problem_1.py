def rotated_list_occurence(rotated_list):

    if len(rotated_list) == 0:
        return 0
    
    right, left = 0, len(rotated_list)-1
    
    if (rotated_list[right] <= rotated_list[left]):
        return 0
    
    while right <= left:
        mid = (right+left)//2

        if mid < left and rotated_list[mid] > rotated_list[mid+1]:
            return mid+1
        if mid > right and rotated_list[mid] < rotated_list[mid-1]:
            return mid
        
        if rotated_list[right] <= rotated_list[left]:
            return right
        
        if rotated_list[mid] >= rotated_list[right]:
            right = mid+1
        else:
            left = mid-1
    return 0
    
        

    

print(rotated_list_occurence([19, 25, 29, 3, 5, 6, 7, 9, 11, 14]) == 3)
print(rotated_list_occurence([1, 2, 3, 4, 5, 6, 7]) == 0)
print(rotated_list_occurence([4]) == 0)