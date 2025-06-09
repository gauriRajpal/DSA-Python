# To find if the given number is palindrome or not.
# It means if the number is same backward and forward 12321

def palindrome(number):
    x=len(number)
    start=0
    end=x-1
    while(start<end):
        if(number[start]==number[end]):
            start+=1
            end-=1
        else:
            return False
    return True

number=[1,2,3,2]
if(palindrome(number)==True):
    print("The number is palindrome")
else:
    print("Number if not palindrome")


# Time complexity:O(n)
# Space complexity:O(1)