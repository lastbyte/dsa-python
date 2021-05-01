
def kth_largest(arr, k):
    heap = []
    for i in range(k):
        heap.append(arr[i])

    min_heapify(heap, 0)
    kth = heap[0]
    print("kth largest till now : "  +str(arr[:i+1]) + " -> " + str(kth))
    for i in range(k, len(arr)):
        kth = heap[0]
        if arr[i] > kth:
            heap.pop(0)
            heap.append(arr[i])
            min_heapify(heap, 0)
        kth = heap[0]
        print("kth largest till now : "  +str(arr[:i+1]) + " -> " + str(kth))


def kth_smallest(arr, k):
    heap = []
    for i in range(k):
        heap.append(arr[i])

    max_heapify(heap, 0)
    kth = heap[0]
    print("kth smallest till now : "  +str(arr[:i+1]) + " -> " + str(kth))
    for i in range(k, len(arr)):
        kth = heap[0]
        if arr[i] < kth:
            heap.pop(0)
            heap.append(arr[i])
            max_heapify(heap, 0)
        kth = heap[0]
        print("kth smallest till now : " +str(arr[:i+1]) + " -> "+ str(kth))

def min_heapify(arr, index):
    if arr is None:
        return

    left = index * 2 + 1
    right = index * 2 + 2

    if left < len(arr):
        min_heapify(arr, left)

    if right < len(arr):
        min_heapify(arr, right)

    if left < len(arr) and arr[index] > arr[left] :
        arr[index], arr[left] = arr[left], arr[index]

    if right < len(arr) and arr[index] > arr[right]:
        arr[index], arr[right], = arr[right], arr[index]


def max_heapify(arr, index):
    if arr is None:
        return

    left = index * 2 + 1
    right = index * 2 + 2

    if left < len(arr):
        max_heapify(arr, left)

    if right < len(arr):
        max_heapify(arr, right)

    if left < len(arr) and arr[index] < arr[left] :
        arr[index], arr[left] = arr[left], arr[index]

    if right < len(arr) and arr[index] < arr[right]:
        arr[index], arr[right], = arr[right], arr[index]



kth_largest([6,9,3,4,5,10,7,8,2], 3)
print()
kth_smallest([6,9,3,4,5,10,7,8,2], 3)

# for k = 3
# largest
#
# 6,9,3 -> (3,6,9) -> 3
# 6,9,3,4 -> (3,4,6,9) -> 4
# 6,9,3,4,5 -> (3,4,5,6,9) -> 5
# 6,9,3,4,5,10 -> (3,4,5,6,9,10) -> 6
# 6,9,3,4,5,10,7 -> (3,4,5,6,7,9,10) -> 7
# 6,9,3,4,5,10,7,8 -> (3,4,5,6,7,8,9,10) -> 8
# 6,9,3,4,5,10,7,8,2 -> (2,3,4,5,6,7,8,9,10) -> 8

# smallest
#
# 6,9,3 -> (3,6,9) -> 9
# 6,9,3,4 -> (3,4,6,9) -> 6
# 6,9,3,4,5 -> (3,4,5,6,9) -> 5
# 6,9,3,4,5,10 -> (3,4,5,6,9,10) -> 5
# 6,9,3,4,5,10,7 -> (3,4,5,6,7,9,10) -> 5
# 6,9,3,4,5,10,7,8 -> (3,4,5,6,7,8,9,10) -> 5
# 6,9,3,4,5,10,7,8,2 -> (2,3,4,5,6,7,8,9,10) -> 4


