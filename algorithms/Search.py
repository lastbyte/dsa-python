class Search:
    def linear_search(self, array, target):
        indexes_found = [
            index for index in range(len(array)) if target == array[index]
        ]
        return indexes_found[0] if len(indexes_found) > 0 else False

    def binary_search(self, arr, target):
        return self.binary_search_util(arr, 0, len(arr) - 1, target)

    def binary_search_util(self, array, start, end, target):
        if start <= end:
            mid = int(start + ((end - start) / 2))
            if array[mid] == target:
                return mid
            if array[mid] > target:
                return self.binary_search_util(array, start, mid - 1, target)
            else:
                return self.binary_search_util(array, mid + 1, end, target)
        return False


if __name__ == "__main__":
    search = Search()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Liner Search : ")
    print("is 10 present in array ? " + str(search.linear_search(arr, 10)))
    print("is 11 present in array ? " + str(search.linear_search(arr, 11)))
    print("Binary Search : ")
    print("is 10 present in array ? " + str(search.binary_search(arr, 10)))
    print("is 11 present in array ? " + str(search.binary_search(arr, 11)))
