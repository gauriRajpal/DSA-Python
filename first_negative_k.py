# Given an array arr[] of integers and a window size k, print the first negative integer in every contiguous subarray of size k.
# If a window doesn't contain a negative integer, output 0 for that window.

from collections import deque

def first_negative_number(arr,k):
    n=len(arr)
    result=[]
    dq=deque()

    for i in range(n):
        if dq and dq[0]<i-k+1:
            dq.popleft()
        if arr[i]<0:
            dq.append(i)
        if i>=k-1:
            if dq:
                result.append(arr[dq[0]])
            else:
                result.append(0)
    return result


arr=[12,-1,-7,8,15,30,16,28]
k=3
print(first_negative_number(arr,k))