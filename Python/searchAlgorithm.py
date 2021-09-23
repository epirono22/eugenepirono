import random 
# Binary Sort
list = [ 8, 9, 1 ,2, 90, 12, 32, 11, 10, 21]

# Sort the list in ascending order: 
list.sort()

print(list)

# Linear search using loops
def linear_search(array, n):
    for i in range(len(array)):
        if n == array[i]:
            return True
    return False


# Binary Search
def binary_search(array, n):
    low = 0
    high = len(array)-1
    mid = 0 
    
    while low <= high:
        mid = (high + low) //2 
        
        # if x is greater than the middle index, then ignore the left half 
        if(array[mid] < n):
            low = mid +1
            
        # if x is smaller than the middle index, then ignore the right half
        elif(array[mid] > n):
            high = mid -1 
        
        # If the mid index is equal to n, then return 
        else: 
            return mid
        
    return mid

