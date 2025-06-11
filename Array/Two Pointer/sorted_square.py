# Given a sorted array of integers(can be negative) we have to return
#  the array of sqaures of each number sorted

##### -----------My idea but wrong-----------

# def square(arr):
#     left=0
#     right=len(arr)-1
#     while(left<=right):
#         if(left==right):
#             arr[right]=arr[right]**2
#             right-=1
#             continue
#         if(abs(arr[left])<abs(arr[right])):
#             arr[right]=arr[right]**2
#             right-=1
#         elif (abs(arr[left])>abs(arr[right])):
#             arr[left],arr[right]=arr[right],arr[left]
#             arr[right]=arr[right]**2
#             right-=1
#     return arr

# print(square([-5,-3,2,4,10]))



#####------CORRECT ONE-------------

def square(arr):
    n=len(arr)
    result=[0]*n
    left=0
    right=n-1
    pos=n-1
    while(left<=right):
        left_sq=arr[left]**2
        right_sq=arr[right]**2
        if left_sq>right_sq:
            result[pos]=left_sq
            left+=1
        else:
            result[pos]=right_sq
            right-=1
        pos-=1
    return result

print(square([-4,-3,-2,-1]))
