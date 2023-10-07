# Runs the main unit test functionality
from functions.unit_test_functions import quick_select_unit_test

length_min = 5
length_max = 50
int_min = 0
int_max = 500
num_of_arrays = 100
duplicates = True

test_results = quick_select_unit_test(length_min, length_max, int_min, int_max, num_of_arrays, duplicates=True)

# Printing results
for test_num, result in test_results.items():
    print(f"For {test_num}, result is: {result}")