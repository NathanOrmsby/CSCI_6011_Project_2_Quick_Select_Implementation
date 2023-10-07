# Runs the main unit test functionality
from functions.unit_test_functions import quick_select_unit_test

# Minimum length of generated array
length_min = 5

# Maximum length of generated array
length_max = 50

# Integer bounds
int_min = 0
int_max = 500

# Number of generated arrays to test
num_of_arrays = 100

# Are duplicates allowed
duplicates = True

# Generate test results
test_results = quick_select_unit_test(length_min, length_max, int_min, int_max, num_of_arrays, duplicates=True)

# Print each test number and result in line by line format
for test_num, result in test_results.items():
    print(f"For {test_num}, result is: {result}")