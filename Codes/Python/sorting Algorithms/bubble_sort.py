import doctest
import time

def bubble_sort(collection):
# bubble_sort functions to sort arrays
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection

#test the code
if __name__ == "__main__":


    doctest.testmod()
   #input
    user_input = input("Enter numbers separated by a comma:").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    #the bubble sort function that we defined earlier
    print(*bubble_sort(unsorted), sep=",")
    print(f"Processing time: {time.process_time() - start}")
