# Python program to find if there are
# two elements wtih given sum

# function to check for the given sum
# in the array
def printPairs(arr, arr_size, sum):
    # Create an empty hash set
    s = set()

    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp in s):
            return ("Pair with given sum {} is {} + {}".format(sum, arr[i], temp))
        s.add(arr[i])


# driver code
A = [1, 4, 45, 6, 10, 150, 8]
n = 160
print(printPairs(A, len(A), n))