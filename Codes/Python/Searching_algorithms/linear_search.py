# If you want to implement Linear Search in python
# Linearly search x in arr[]
# If x is present then return its location
# else return -1

def linear_search(arr, x):
    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1

# Test array
arr = [43, 55, 34, 343, 4, 3, 4323]
x = 34
result = linear_search(arr, x)
print(result)