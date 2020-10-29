#Python program to check if arr2 is subset of arr1

def func(arr1, arr2, arr1_size, arr2_size):

#create a  hashtable
    hash = {}
    for i in arr1:
        if i not in hash:
            hash[i]=1
        else:
            hash[i] += 1

#loop through each element of arr_2 and check if it is in hash
    for j in range(arr2_size):
        if arr2[j] not in hash:
            return False

    return True

#driver code
arr1 = [1,2,3,49,4,5]
arr2 = [5,3,4]
arr1_size = len(arr1)
arr2_size = len(arr2)
print(func(arr1, arr2, arr1_size, arr2_size))



