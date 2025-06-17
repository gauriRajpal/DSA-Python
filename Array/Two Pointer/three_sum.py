# Given an array of integer return all unique triplets such that they are thier sum is 0

def triplets(arr):
    arr.sort()
    result=[]
    n=len(arr)

    for i in range (n-2):
        if i>0 and arr[i]==arr[i-1]:
            continue

        target=-arr[i]
        left,right=i+1,n-1

        while left<right:
            current_sum=arr[left]+arr[right]

            if current_sum==target:
                result.append([arr[i],arr[left],arr[right]])
                while left<right and arr[left]==arr[left+1]:
                    left+=1
                while left<right and arr[right]==arr[right-1]:
                    right-=1
                left+=1
                right-=1
            elif current_sum<target:
                left+=1
            else:
                right-=1
    return result

print(triplets([-1,0,1,2,-1,-4]))