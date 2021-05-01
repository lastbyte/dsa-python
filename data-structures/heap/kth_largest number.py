
def kth_largest(arr, k):
    heap = []
    for i in range(k):
        heap.append(arr[i])

    heapify(heap, 0)

    for i in range(k, len(arr)):
        print("kth largest till now : " + str(heap.pop(0)))
        heap.append(arr[i])
        heapify(heap, 0)


def heapify(arr, index):
    if arr is None:
        return

    left = index * 2 + 1
    right = index * 2 + 2

    if left < len(arr):
        heapify(arr, left)

    if right < len(arr):
        heapify(arr, right)

    if left < len(arr) and arr[index] > arr[left] :
        arr[index], arr[left] = arr[left], arr[index]

    if right < len(arr) and arr[index] > arr[right]:
        arr[index], arr[right], = arr[right], arr[index]



kth_largest([6,9,3,4,5,10,7,8,2], 3)