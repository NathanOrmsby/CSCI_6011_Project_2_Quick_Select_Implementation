# Plotting and line of best fit
from functions.time_complexity_analysis_functions import plot_time_complexity_graph

num_arrays = 100
smallest_array_length = 5
k_value = smallest_array_length // 2 + 1

slope, intercept, r_squared = plot_time_complexity_graph(num_arrays, smallest_array_length, k_value)

# Print results
print(f"Line of best fit: y = {slope:.4f}x + {intercept:.4f}")
print(f"Coefficient of determination (R^2): {r_squared:.4f}")

