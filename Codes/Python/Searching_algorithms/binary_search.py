# It returns index of n in given array arr if present,
# else returns -1
def binary_search(arr, n):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Check if n is present at mid-pos
        if arr[mid] < n:
            low = mid + 1

        # If n is greater, remove left half
        elif arr[mid] > n:
            high = mid - 1

        # If n is smaller, remove right half
        else:
            return mid

        # If the loop ends, then the element was not found
    return -1


# Test array
arr = [4,4,34,35,4,324,6,4,3,43,342]
n = 342

result = binary_search(arr, n)
print(result)