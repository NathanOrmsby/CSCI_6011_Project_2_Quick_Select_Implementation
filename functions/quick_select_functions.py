# Median of medians sub functions

# Split array into groups of 5
def generate_groups_of_5(start, end):
    """
    Taking an array defined as [arr[start], ... , arr[end]], returns groups of (subarray_start, subarray_end) pointers to each subarray of length 5 within arr.
    """
    res = []
    for i in range(start, end + 1, 5):
        subarray_start = i
        subarray_end = min(i + 4, end)
        res.append([subarray_start, subarray_end])
    return res

# Insertion sort functions
def pointer_insertion_sort(arr, start, end):
    """
    Insertion sort an array in place between two pointers start and end.
    """
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1
        while j >= start and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def sort_all_subarrays(arr, pointer_arr):
    """
    Takes an array of integers and sorts all subarrays as defined by pointer_arr - [[start0, end0], [start1, end1], ...]
    """
    for pointers in pointer_arr:
        start = pointers[0]
        end = pointers[1]
        pointer_insertion_sort(arr, start, end)

# Functions for finding median
def find_median_index_of_sorted_subarray(arr, start, end):
    """
    Finds and returns absolute index of median within subarray defined [arr[start], ..., arr[end]]
    """
    arr_length = end - start + 1
    # Odd length array: Median is center value
    if arr_length % 2 == 1:
        median_offset = arr_length // 2
        median_index = start + median_offset
    # Even length array: Choose lower index median approximation
    else:
        lower_median_offset = (arr_length - 1) // 2
        median_index = start + lower_median_offset
    return median_index
    
def find_sorted_subarray_median_indexes(arr, pointer_arr):
    """
    Returns an array of pointers to median values within sorted subarrays as defined by pointer_arr.
    """
    median_indexes = []
    for pointers in pointer_arr:
        start = pointers[0]
        end = pointers[1]
        subarray_median_index = find_median_index_of_sorted_subarray(arr, start, end)
        median_indexes.append(subarray_median_index)
    return median_indexes  

# Swapping to front
def swap_ordered_indexes_to_front(arr, start, index_list):
    """
    Given an array, and a sorted list of indexes. Swaps every indexed element to the front of the array.
    """
    index_list_len = len(index_list)
    for i in range(start, start + index_list_len):  
        index_list_index = i - start
        index = index_list[index_list_index]
        arr[i], arr[index] = arr[index], arr[i]

# ----------------------------------------------------------------------------------------------------------------------------------------- #
        
# Median of medians
def median_of_medians(arr, start, end):
    """
    Median of medians recursive algorithm
    """
    # Base case: Just sort and return median if length <= 5
    arr_length = end - start + 1
    if arr_length <= 5:
        pointer_insertion_sort(arr, start, end)
        subarray = arr[start:end + 1]
        median_offset = arr_length // 2
        median_index = start + median_offset
        median = arr[median_index]    
        return median_index
    
    # Generate groups of 5
    subarray_pointers = generate_groups_of_5(start, end)
    
    # Insertion sort each subarray
    sort_all_subarrays(arr, subarray_pointers)
    
    # Extract indexes of medians
    median_indexes = find_sorted_subarray_median_indexes(arr, subarray_pointers)
    
    # Swap median values to the front of the array
    swap_ordered_indexes_to_front(arr, start, median_indexes)
    
    # Recursive call
    median_arr_end_offset = len(median_indexes) - 1
    median_arr_end = start + median_arr_end_offset
    return median_of_medians(arr, start, median_arr_end)

# ----------------------------------------------------------------------------------------------------------------------------------------- #

# Quick select functionality

# Partition
def partition(arr, start, end, pivot_index):
    """
    Lomuto partition of an array about a provided ideal pivot found using the median of medians algorithm.
    Returns the final index of the pivot after partitioning array
    """
    pivot = arr[pivot_index]
    
    # Move pivot to end of array for convenience
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    # Start partition of array about pivot
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Move pivot to correct position
    final_pivot_index = i + 1
    arr[final_pivot_index], arr[end] = arr[end], arr[final_pivot_index]
    return final_pivot_index

# ----------------------------------------------------------------------------------------------------------------------------------------- #

# Overall main function
# Quick select: kth smallest algorithm
def quick_select_kth_smallest(arr, start, end, k):
    """
    Finds the kth smallest value of an array using the quick select and median of medians algorithm.
    """
    # Find ideal pivot using median of medians
    ideal_pivot_index = median_of_medians(arr, start, end)
    
    # Partition the array about the pivot
    final_pivot_index = partition(arr, start, end, ideal_pivot_index)
    
    # Compare the pivot index with k 
    zero_indexed_k = k - 1
    if final_pivot_index < zero_indexed_k:
        return quick_select_kth_smallest(arr, final_pivot_index + 1, end, k)
    elif final_pivot_index > zero_indexed_k:
        return quick_select_kth_smallest(arr, start, final_pivot_index - 1, k)
    else:
        return arr[final_pivot_index]