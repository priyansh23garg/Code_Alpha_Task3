def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    while start<=end:
        mid = (start + end) // 2          
        if(arr[mid] == target):
            return mid  
        elif(arr[mid]<target):
            start = mid + 1 
        else:
            end = mid - 1
    return -1

sorted_array = eval(input("Enter a sorted array:"))
target_value = int(input("Enter the target value:"))

result = binary_search(sorted_array, target_value)
if result!=-1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")
