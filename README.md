# Code_Alpha_Task3
# Binary Search Algorithm

This Python script demonstrates the implementation of the **Binary Search** algorithm. Binary search is an efficient algorithm for finding a specific value in a sorted array.

## How It Works

1. **Input:**
    - The `binary_search` function takes a sorted array (`arr`) and a target value (`target`) as input.
    - Users are prompted to enter a sorted array and the target value.

2. **Binary Search:**
    - The function uses the binary search algorithm to find the target value in the sorted array.
    - It starts by defining two pointers, `start` and `end`, representing the start and end indices of the array.
    - It repeatedly calculates the middle index (`mid`) and compares the middle element with the target value.
    - If the middle element is equal to the target, the index of the target is returned.
    - If the middle element is less than the target, the search continues in the right half of the array.
    - If the middle element is greater than the target, the search continues in the left half of the array.
    - If the target is not found, the function returns `-1`.

3. **Output:**
    - The script prints the index of the target value if found.
    - If the target value is not in the array, it prints a message indicating that the element was not found.

## Example

```
Enter a sorted array: [1, 3, 5, 7, 9, 11, 13, 15]
Enter the target value: 7
Element found at index 3
```
