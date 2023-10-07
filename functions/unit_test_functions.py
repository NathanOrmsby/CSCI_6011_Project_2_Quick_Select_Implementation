# Unit test functionalities for the quick select and median of medians algorithms
import random 

from functions.quick_select_functions import quick_select_kth_smallest

# Sub functions
def generate_random_arrays(length_min, length_max, int_min, int_max, num_of_arrays):
    """
    Returns a list of arrays of length_min <= random length <= length_max, with values between int_min and int_max inclusive.
    num_of_arrays is the number of arrays that will be generated, all arrays will be shuffled.
    """
    list_of_arrays = []
    array_lengths = [random.randint(length_min, length_max) for i in range(num_of_arrays)]
    for array_length in array_lengths:
        generated_array = [random.randint(int_min, int_max) for i in range(array_length)]
        list_of_arrays.append(generated_array)
    return list_of_arrays

def generate_random_unique_arrays(length_min, length_max, int_min, int_max, num_of_arrays):
    """
    Returns a list of arrays not containing duplicates of length_min <= random length <= length_max, with values between int_min and int_max inclusive.
    num_of_arrays is the number of arrays that will be generated, all arrays will be shuffled.
    """

    if length_max >= (int_max - int_min) - 1:
        raise ValueError("The length of a unique array cannot be greater than or equal to (int_max - int_min) - 1")
    
    list_of_arrays = []
    for i in range(num_of_arrays):
        array_length = random.randint(length_min, length_max)
        generated_array = []
        generated_numbers = set()
        while len(generated_array) < array_length:
            num = random.randint(int_min, int_max)
            if num not in generated_numbers:
                generated_array.append(num)
                generated_numbers.add(num)
        list_of_arrays.append(generated_array)
    return list_of_arrays

def generate_random_k_values(list_of_arrays):
    """
    Returns a list of random k values for each array in list_of_arrays.
    """
    k_list = []
    for arr in list_of_arrays:
        k = random.randint(1, len(arr))
        k_list.append(k)
    return k_list

def assert_quick_select(arr, k):
    """
    Asserts whether quick select results in the correct kth smallest for a single array.
    """
    # Sort array and find kth smallest
    zero_indexed_k = k - 1
    sorted_arr = sorted(arr)
    true_kth_smallest = sorted_arr[zero_indexed_k]
    
    # Experimental kth smallest using quick select
    arr_copy = list(arr)
    experimental_kth_smallest = quick_select_kth_smallest(arr_copy, 0, len(arr_copy) - 1, k)
    return true_kth_smallest == experimental_kth_smallest

# -------------------------------------------------------------------------------------------------------------- #

# Main unit test function
def quick_select_unit_test(length_min, length_max, int_min, int_max, num_of_arrays, duplicates=True):
    """
    Returns a dictionary of test results of the quick select algorithm over a defined number of arrays containing randomly generated integers and of random lengths
    bounded by the parameters. K_Values are randomized for each array.
    Set duplicates to True to test over arrays allowing duplicate integer values, otherwise False to test over arrays containing only unique integer values.

    Warning: If using unique integer values, length_max cannot be greater than (int_max - int_min) - 1. Otherwise a value error will be raised, or program behavior may be 
    undefined.
    """
    test_results = {}
   
    # Generate list of arrays
    if duplicates:
        list_of_arrays = generate_random_arrays(length_min, length_max, int_min, int_max, num_of_arrays)
    else:
        list_of_arrays = generate_random_unique_arrays(length_min, length_max, int_min, int_max, num_of_arrays)
    
    # Generate list of k values
    k_vals = generate_random_k_values(list_of_arrays)
    
    # Perform the unit tests
    iteration_count = 0
    for i in range(len(list_of_arrays)):
        iteration_count += 1
        arr = list_of_arrays[i]
        k = k_vals[i]
        test_result = assert_quick_select(arr, k)
        # Add to result dictionary
        arr_string = f"Test {i}"
        test_results[arr_string] = test_result

    return test_results