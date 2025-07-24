# Given an array of intger nums and an intger k.
# Find the maximum sum of the contiguous subarray pf size k

def max_sum_subarray(nums,k):
    window_sum=0
    max_sum=float('-inf')    # We have written '-inf' because there can be all negative numbers in the array so to resolve it

    for i in range(len(nums)):
        window_sum+=nums[i]

        if i>=k-1:
            max_sum=max(window_sum,max_sum)
            window_sum-=nums[i-k+1]

    return max_sum

nums = [2, -1, -5, 1, 3, 2]
k=3
print(max_sum_subarray(nums,k))