
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

arr = [9, 1, 6, 2, 5, 3, 4, 8, 7]

print(bubble_sort(arr))
print(insertion_sort(arr))
print(selection_sort(arr))
