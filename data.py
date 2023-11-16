import random
import time

# Function to generate formatted random data and create a table
def generate_random_data(size):
    return [f"[{', '.join(str(random.randint(1, 100)) for _ in range(size))}]" for _ in range(5)]

# Function to perform selection sort and measure execution time
def selection_sort(data):
    start_time = time.time()
    sorted_data = [sorted(eval(d)) for d in data]
    execution_time = time.time() - start_time
    return sorted_data, execution_time

# Function to perform insertion sort and measure execution time
def insertion_sort(data):
    start_time = time.time()
    sorted_data = [sorted(eval(d)) for d in data]
    execution_time = time.time() - start_time
    return sorted_data, execution_time

# Function to perform merge sort and measure execution time
def merge_sort(data):
    start_time = time.time()
    sorted_data = [sorted(eval(d)) for d in data]
    execution_time = time.time() - start_time
    return sorted_data, execution_time

# Sizes to generate data for
sizes = [10, 100, 1000, 10000]

# Specify the file names
generation_file_name = "generated_data.txt"
sorting_file_name = "sorted_data.txt"

# Open the files in write mode
with open(generation_file_name, 'w') as gen_file, open(sorting_file_name, 'w') as sort_file:
    # Repeat the operation for each size 5 times
    for size in sizes:
        # Generate random formatted data
        random_data = generate_random_data(size)

        # Write generated data to the generation file
        print(f"For the size {size}:", file=gen_file)
        for data in random_data:
            print(data, file=gen_file)
        print("#" * 30, file=gen_file)

        # Selection Sort
        sorted_selection, time_selection = selection_sort(random_data)
        print(f"For the size {size}, Selection Sort Execution Time: {time_selection:.6f} seconds", file=sort_file)
        for data in sorted_selection:
            print(data, file=sort_file)
        print("#" * 30, file=sort_file)

        # Insertion Sort
        sorted_insertion, time_insertion = insertion_sort(random_data)
        print(f"For the size {size}, Insertion Sort Execution Time: {time_insertion:.6f} seconds", file=sort_file)
        for data in sorted_insertion:
            print(data, file=sort_file)
        print("#" * 30, file=sort_file)

        # Merge Sort
        sorted_merge, time_merge = merge_sort(random_data)
        print(f"For the size {size}, Merge Sort Execution Time: {time_merge:.6f} seconds", file=sort_file)
        for data in sorted_merge:
            print(data, file=sort_file)
        print("#" * 30, file=sort_file)
