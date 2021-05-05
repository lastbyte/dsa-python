def linear_search(array, target):
    indexes_found = [index for index in range(len(array)) if target == array[index]]
    return True if len(indexes_found) > 0 else False
