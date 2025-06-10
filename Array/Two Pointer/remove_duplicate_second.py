# In this we would allow at most 2 occurrence of the element 
# Have to return the length after the removal

def duplicate(arr):
    if len(arr)<2:
        return len(arr)
    
    left=2
    for right in range(2,len(arr)):
        if(arr[right]!=arr[left-2]):
            arr[left]=arr[right]
            left+=1

    return left

arr=[1,1,1,2,2,3]
k=duplicate(arr)
print(f'The left after removal: {k}')
print(f"The array is: {arr[:k]}")