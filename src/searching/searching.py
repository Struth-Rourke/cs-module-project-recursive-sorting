# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # identify the midpoint
    mid = int((start + end) / 2)
    
    # check for the array size and make sure it's greater than 1 -- meaning it's
    # not empty
    if start >= end:
        return -1
    
    # return the mid index if it is target
    if arr[mid] == target:
        # return mid index
        return mid

    # if the mid value is less than the target (go right side)
    if arr[mid] < target:
        # recursively call the function and change the start to reflect where
        # tne midpoint is -- the end stays the same since we are on the right
        # side of the tree
        return binary_search(arr, target, mid, end)
    # else: the mid value is greater than the target (go left side)
    else:
        # recursively call the function and change the end to reflect where
        # tne midpoint is -- the start stays the same since we are on the left
        # side of the tree
        return binary_search(arr, target, start, mid)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
