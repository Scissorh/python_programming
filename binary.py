def binary_search(arr , target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1,2,3,4,5,6,7,8,9]
target = 5 

result=binary_search(arr, target)

if result != -1:
    print(f" elemet {target} found at index {result}")
else:
    print(f" elemet {target} not found")

