# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0

    for i in range(0, elements):
        # if all elements in arrA have been merged, put next element in arrB into merged_arr
        if len(arrA) <= a:
            merged_arr[i] = arrB[b]
            b += 1
        # if all elements in arrB have been merged, put next element in arrA into merged_arr
        elif len(arrB) <= b:
            merged_arr[i] = arrA[a]
            a += 1
        # if next element in arrA is smaller, add to merged array
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        # if next element in arrB is smaller, add to merged array
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


print(merge([4, 99, 13, 75, 2, 1, 178, 81], [3, 74, 11]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
