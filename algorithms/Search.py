

def search(array, target):
    indexes_found = [ index for index in range(len(array)) if target == array[index] ]
    return True if len(indexes_found) > 0 else False


def binary_search(array, start, end, target):
    if start <= end:
        mid = int(start + ((end - start)/2))
        if array[mid] == target:
            return True
        if array[mid] > target:
            return binary_search(array, start, mid-1, target)
        else:
            return binary_search(array, mid+1, end, target)
    return False


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Liner Search : ")
    print("is 10 present in array ? " + str(search(arr, 10)))
    print("is 11 present in array ? " + str(search(arr, 11)))
    print("Binary Search : ")
    print("is 10 present in array ? " + str(binary_search(arr, 0, len(arr) - 1,  10)))
    print("is 11 present in array ? " + str(binary_search(arr, 0, len(arr) - 1, 11)))


