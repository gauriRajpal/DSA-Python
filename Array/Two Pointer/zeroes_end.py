# Move all zeroes to the end of the array

# ######---------MY THOUGHTS--------------

def end(arr):
    left=0
    for right in range(len(arr)):
        if(arr[right]!=0):
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
    return arr

arr=[0,1,0,3,12]
print(f'After pushing: {end(arr)}')


# # But there is a problem we can it swaps even when left==right
# # So we can add a conditional statement after if(arr[right]!=0)
# # :if left!=right :

#########--------ONLINE-------------------

# First place all the non-zeroes at front
# Then in the end place the zeroes

# def end(arr):
#     left=0
#     for right in range(len(arr)):
#         if arr[right]!=0:
#             arr[left]=arr[right]
#             left+=1
    
#     for right in range(left,len(arr)):
#         arr[right]=0

#     return arr

# print(f'After performing: {end([0,1,0,3,12])}')