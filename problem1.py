#Question Given K sorted arrays of size N each, the task is to merge them all maintaining their sorted order.

def merge_sorted_arrays():
    # Input the number of arrays and their size
    num_arrays = int(input("Enter the number of arrays (K): "))
    array_size = int(input("Enter the size of each array (N): "))
    
    input_arrays = []
    merged_result = []

    def optimized_merge_sort(arr):
        """
        Perform an optimized merge sort on the given array.
        This function is more efficient than insertion sort for larger arrays.
        """
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = optimized_merge_sort(arr[:mid])
        right = optimized_merge_sort(arr[mid:])
        
        return merge(left, right)

    def merge(left, right):
        """
        Merge two sorted arrays into a single sorted array.
        """
        result = []
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # Input the sorted arrays
    for i in range(num_arrays):
        array = list(map(int, input(f"Enter sorted array {i+1}: ").split()))
        input_arrays.append(array)

    # Merge all input arrays
    for array in input_arrays:
        merged_result.extend(array)

    # Sort the merged array
    sorted_result = optimized_merge_sort(merged_result)

    print("Merged array in sorted order:", sorted_result)

# Run the function
merge_sorted_arrays()

'''
Example/Result:
Enter the number of arrays (K): 3
Enter the size of each array (N): 4
Enter sorted array 1: 1 3 5 7
Enter sorted array 2: 2 4 6 8
Enter sorted array 3: 0 9 10 11
Merged array in sorted order: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Enter the number of arrays (K): 3
Enter the size of each array (N): 3
Enter sorted array 1: 1 3 7
Enter sorted array 2: 2 4 8
Enter sorted array 3: 9 10 11
Merged array in sorted order: [1, 2, 3, 4, 7, 8, 9, 10, 11]
'''
