def reverse_list(arr,k):
    n=len(arr)
    for i in range(0,n,k):
        left=i
        right=min(i+k-1,n-1)       # Finds the limit if the number if less than would go to end
        while(left<right):
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    return arr


arr=[1,2,3,4,5,6,7,8]

print(f"Reversed: {reverse_list(arr,3)}")