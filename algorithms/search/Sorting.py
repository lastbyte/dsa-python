
def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array ) - i -1):
            if array[j] > array[ j +1]:
                array[j], array[ j +1] = array[ j +1], array[j]
    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        elem = array[i]
        j = i-1
        while j >= 0 and elem < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = elem
    return array


def selection_sort(array):
    for i in range(0, len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j;
        array[i], array[min_index] = array[min_index], array[i]
    return array


def merge_sort(array, left, right):
    if left<right:
        mid = int(left + ((right - left)/2))
        merge_sort(array, left, mid)
        merge_sort(array, mid+1, right)
        merge(array, left, mid, right)


def merge(array, left, mid, right):
    i, j, k = left, mid+1, 0
    tmp_arr = [0] * (right-left+1)
    while i <= mid and j <= right:
        if array[i] < array[j]:
            tmp_arr[k] = array[i]
            i = i+1
        else:
            tmp_arr[k] = array[j]
            j = j+1
        k = k+1

    while i <= mid:
        tmp_arr[k] = array[i]
        i = i + 1
        k = k + 1

    while j <= right:
        tmp_arr[k] = array[j]
        j = j+1
        k = k+1

    for i in range(len(tmp_arr)):
        array[left + i] = tmp_arr[i]


def quicksort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot-1)
        quicksort(arr, pivot+1, right)


def partition(arr, left, right):
    pivot = left
    correct_pivot = left

    for i in range(left, right+1):
        if arr[i] < arr[pivot]:
            correct_pivot = correct_pivot+1
            arr[i], arr[correct_pivot] = arr[correct_pivot], arr[i]

    arr[correct_pivot], arr[pivot] = arr[pivot], arr[correct_pivot]
    return correct_pivot


if __name__ == "__main__":
    arr = [-10, 9, 1, 6, 2, 5, 3, 4, 8, 7, -5 , -1, -4]
    print("original array : " + str(arr))
    print("sorted array (Bubble sort) : " + str(bubble_sort(arr)))
    arr = [-10, 9, 1, 6, 2, 5, 3, 4, 8, 7, -5 , -1, -4]
    print("sorted array (insertion sort) : " + str(insertion_sort(arr)))
    arr = [-10, 9, 1, 6, 2, 5, 3, 4, 8, 7, -5 , -1, -4]
    print("sorted array (Selection sort) : " + str(selection_sort(arr)))
    arr = [-10, 9, 1, 6, 2, 5, 3, 4, 8, 7, -5 , -1, -4]
    merge_sort(arr, 0, len(arr)-1)
    print("sorted array (Merge sort) : " + str(arr))

    arr = [-10, 9, 1, 6, 2, 5, 3, 4, 8, 7, -5 , -1, -4]
    quicksort(arr, 0, len(arr) - 1)
    print("sorted array (Quick sort) : " + str(arr))
