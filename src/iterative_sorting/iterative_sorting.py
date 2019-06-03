# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_index = current_index
        # Find next smallest element
        for j in range(current_index, len(arr)):
            if arr[j] <= arr[smallest_index]:
                smallest_index = j

        # swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[current_index]
        arr[current_index] = temp
    return arr


# print(selection_sort([2, 9, 3]))


# TO-DO:  Implement the Bubble Sort function below
def bubble_sort(arr):

    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                # swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

    return arr


# print(bubble_sort([2, 3, 8, 5, 6, 85, 13]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr