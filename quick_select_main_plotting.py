# Plotting and line of best fit
from functions.time_complexity_analysis_functions import plot_time_complexity_graph

# Number of arrays that will be generated
num_arrays = 100

# Smallest array length, largest array length will be num_arrays * smallest_array_length
smallest_array_length = 5

# K value
k_value = smallest_array_length // 2 + 1

# Generates the plot, and returns the line of best fit information
slope, intercept, r_squared = plot_time_complexity_graph(num_arrays, smallest_array_length, k_value)

# Print line of best fit and coefficient of determination (goodness of fit)
print(f"Line of best fit: y = {slope:.4f}x + {intercept:.4f}")
print(f"Coefficient of determination (R^2): {r_squared:.4f}")

