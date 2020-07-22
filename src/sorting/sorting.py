# # Bubble Sort -- recursively
# def recursive_bubble_sort(arr, unsorted_length):
#     # loop through the unsorted_length
#     for i in range(unsorted_length - 1):
#         # if the array value is greater than the one ahead of it
#         if arr[i] > arr[i + 1]:
#             # switch the places
#             arr[i], arr[i +1] = arr[i + 1], arr[i]

#         # if n - 1 of the list (making sure there is nothing to the right of the 
#         # last element) is more than 1 -- meaning there is more than 1 element 
#         # in the remaining list
#         if unsorted_length - 1 > 1:
#             # recursively call the function again on the parred down list
#             recursive_bubble_sort(arr, unsorted_length - 1)

# ## CHECK:
# # a = [1,6,2,7,3,8,4,9,5,10]
# # recursive_bubble_sort(a, 10)



# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # instantiating empty list that will hold values
    merged_arr = []

    # instantiating arrA_idx and arrB_idx value
    arrA_idx = 0
    arrB_idx = 0

    # while the arrA_idx, arrB_idx are less than the len of arrA, arrB
    while arrA_idx < len(arrA) and arrB_idx < len(arrB):
        # if the arrA value with arrA_idx <= the arrB value with arrB_idx 
        if arrA[arrA_idx] <= arrB[arrB_idx]:
            # append the value to the merged_arr empty list
            merged_arr.append(arrA[arrA_idx])
            # increase arrA_idx
            arrA_idx += 1
        # else:
        else:
            # append the value to the merged_arr empty list
            merged_arr.append(arrB[arrB_idx])
            # increase arrB_idx
            arrB_idx += 1

    # while the arrA_idx is < len(arrA)
    while arrA_idx < len(arrA):
        # append to merged_arr with the appropriate arrA_idx
        merged_arr.append(arrA[arrA_idx])
        # increase arrA_idx
        arrA_idx += 1

    # while the arrB_idx is < len(arrB)
    while arrB_idx < len(arrB):
        # append to merged_arr with the appropriate arrB_idx
        merged_arr.append(arrB[arrB_idx])
        # increase arrB_idx
        arrB_idx += 1

    # return the merged_arr
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # get the midpoint of the array
    mid = len(arr) // 2
    # get the lefthand side of the array
    left = arr[:mid]
    # get the righthand side of the array
    right = arr[mid:]
    # base case: if array contains a single element, it is already sorted
    if len(arr) <= 1:
        # return the array
        return arr
    # else
    else:
        # recursively, call the merge function on the left and right sides of
        # the array distributions; and return the output
        return merge(merge_sort(left), merge_sort(right))

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here
