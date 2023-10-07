# Time complexity analysis

import time
import random
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

from functions.quick_select_functions import quick_select_kth_smallest

# ----------------------------------------------------------------------------------------------------------------------------------------- #

# Sub functions

def generate_random_array(length, int_min, int_max):
    """
    Returns an array with random integers between int_min and int_max with defined length.
    """
    return [random.randint(int_min, int_max) for i in range(length)]


def quickselect_time_complexity(arr, start, end, k):
    """
    Returns time in nanoseconds for quick select to complete
    """
    start_time = time.perf_counter()
    quick_select_kth_smallest(arr, start, end, k)
    end_time = time.perf_counter()
    elapsed_time_ns = (end_time - start_time) * 1e9  # Multiply by 1e9 to convert seconds to nanoseconds
    return elapsed_time_ns    

def generate_array_lengths(num_arrays, smallest_array_length):
    """
    Generates a list of array lengths where the length is multiples of the smallest_array_length depending on the index.
    """
    array_lengths = [(i + 1) * smallest_array_length for i in range(num_arrays)]
    return array_lengths

def quickselect_time_complexity_graph_data(num_points, array_lengths, k_value):
    """
    Given a number of arrays (num_points) and a smallest array size, returns a list of execution time data points for the 
    quick select kth smallest algorithm on a random array of each size.
    """
    # Generate random arrays
    int_min = 0
    int_max = array_lengths[-1]
    arrays = [generate_random_array(array_length, int_min, int_max) for array_length in array_lengths]
    
    # Get time complexity data
    time_complexity_data = [quickselect_time_complexity(array, 0, len(array) - 1, k_value) for array in arrays]
    return time_complexity_data

# ----------------------------------------------------------------------------------------------------------------------------------------- #

# Main functionality
def plot_time_complexity_graph(num_points, smallest_array_length, k_value):
    """
    Plots execution times of the quick select algorithm against array lengths, saving the plot to the local directory as "time_complexity_quick_select.png" 
    Also computes the line of best fit for the given data and returns the slope, intercept, and R^2 value.
    """
    # Generate array lengths
    array_lengths = generate_array_lengths(num_points, smallest_array_length)
    
    # Get data
    time_complexity_data = quickselect_time_complexity_graph_data(num_points, array_lengths, k_value)
    
    # Plot data
    plt.plot(array_lengths, time_complexity_data, marker='o', linestyle='-', color='b')
    
    # Titles and labels
    plt.title("Time Complexity of QuickSelect")
    plt.xlabel("Array Length")
    plt.ylabel("Execution Time (nanoseconds)")
    
    # Save graph
    plot_name = "time_complexity_quick_select.png"
    plt.savefig(plot_name)
    
    # Compute line of best fit
    slope, intercept = np.polyfit(array_lengths, time_complexity_data, 1)
    
    # Compute R^2 value
    _, _, r_value, _, _ = stats.linregress(array_lengths, time_complexity_data)
    r_squared = r_value**2
    
    return slope, intercept, r_squared