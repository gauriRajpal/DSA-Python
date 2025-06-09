# To remove duplicated values from sorted array

def duplicate(num):
    if not num:
        return 0
    left=1
    for right in range(1,len(num)):
        if(num[right]!=num[right-1]):
            num[left]=num[right]
            left+=1
    
    return left

print(duplicate([1,2,3,3,4]))


# Here we move the right pointer checking and the left pointer is kept for position

# We compare the current right with the previous one and both are same then we move
# the right pointer keeping the left one at the same positon

# When the current right and the previous one are not same then we write the value
# of the right pointer in the left one and move the left pointer by one

# In the end we return the left pointer value
