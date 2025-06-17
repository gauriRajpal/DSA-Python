# Given an non-negative integer and we have to find the maximum area which could be 
# contained by two lines.
# Taking one end point (i,0) and the other (i,height[i])


def container(arr):
    left=0
    right=len(arr)-1
    max_area=0

    while(left<right):
        width=right-left
        h=min(arr[left],arr[right])
        area=width*h

        max_area=max(max_area,area)

        if arr[left]<arr[right]:
            left+=1
        else:
            right-=1
    
    return max_area

print(container([1,8,6,2,5,4,8,3,7]))