#Question Given a sorted array array of size N, the task is to remove the duplicate elements from the array.

def remove_duplicates(sorted_arr):
    if not sorted_arr:
        return []
    # An empty array or single-element array has no duplicates
    
    array_length = len(sorted_arr)
    unique_index = 0
    
    for current_index in range(1, array_length):
        if sorted_arr[current_index] != sorted_arr[unique_index]:
            unique_index += 1
            sorted_arr[unique_index] = sorted_arr[current_index]
    
    return sorted_arr[:unique_index + 1]

# Get input from user
input_string = input("Enter a sorted array: ")
original_array = list(map(int, input_string.split()))

# Remove duplicates
deduplicated_array = remove_duplicates(original_array)

# Print results
print(f"Array after removing the duplicate elements: {deduplicated_array}")

"""
Example:
Enter a sorted array: 2 2 2 2 2
Array after removing the duplicate elements: [2]

Enter a sorted array: 1 2 2 3 4 4 4 5 5
Array after removing the duplicate elements: [1, 2, 3, 4, 5]
"""