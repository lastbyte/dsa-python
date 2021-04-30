

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
