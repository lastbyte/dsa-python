from binary_search import *
from linear_search import *


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Liner Search : ")
    print("is 10 present in array ? " + str(linear_search(arr, 10)))
    print("is 11 present in array ? " + str(linear_search(arr, 11)))
    print("Binary Search : ")
    print("is 10 present in array ? " + str(binary_search(arr, 0, len(arr) - 1,  10)))
    print("is 11 present in array ? " + str(binary_search(arr, 0, len(arr) - 1, 11)))


