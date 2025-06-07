arr=[1,2,3,4,5]

####-------------Traversal of elements-----------

# for num in arr:     # Prints all the numbers
#     print(num)

# for i in range(len(arr)):       # Travelling elements one by one
#     print(f"Index {i}, value {arr[i]}")



####-----------Inserting an element ---------------------------

# arr.append(7)       # Inserts at last position
# print(arr)

# arr.insert(2,10)       #Inserts at specific position (position,value)
# print(arr)

#####----------DELETING ELEMENTS----------------------

# From specific value
# arr.remove(1)
# print(arr)

# # From index
# del arr[0]
# print(arr)

# #Removes the last element and returns it's
# print(arr.pop())
# print(arr)

######----------SEARCHING--------------

# Searches if 3 exists in array. Returns true if found

# print(13 in arr)

# # Getting index for a particular element. If the element does not exist gives error
# try:
#     print(arr.index(14))
# except Exception as e:
#     print("Element not found")



#####------------UPDATING THE ELEMENTS------
# arr[0]=100
# print(arr)