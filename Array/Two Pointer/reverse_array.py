# # Given an array of integer reverse the array in-place without using reverse() or 
# # without creating a new array


# def reverse_list(arr):
#     left=0
#     right=len(arr)-1
#     while left<right :
#         temp=arr[left]
#         arr[left]=arr[right]
#         arr[right]=temp
#         # arr[left],arr[right]=arr[right],arr[left]
#         left=left+1
#         right=right-1
#     return arr

# arr=[1,2,3,4,5]
# print(f"Reversed:",reverse_list(arr))

# # Time complexity= O(n)->Each element visited once
# # Space complexity =O(1)-> in-place no extra space


####------------REVERSING A SUBARRAY----------
def reverse_list(arr,start,end):
    left=start-1
    right=end-1
    while(left<right):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

arr=[1,2,3,4,5,6,7,8,9]
print(f"Reversed :{reverse_list(arr,2,5)}")