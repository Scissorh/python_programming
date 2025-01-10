def moves_zero(arr):
    last_non_zero_index = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[last_non_zero_index] = arr[last_non_zero_index], arr[i]
            last_non_zero_index += 1

arr1 = [1,2,0,3,4,0]
moves_zero(arr1)
print(arr1)
    
