# Remove all the occurence of the element given from the array and return the length
# It should be in-place

def occurrence(arr,val):
    left=0
    for right in range(0,len(arr)):
        if(arr[right]!=val):
            arr[left]=arr[right]
            left+=1
    return left


arr=[3,2,2,3]
k=occurrence(arr,3)
print(f'Length after reversal: {k}')
print(f'After removing: {arr[:k]}')