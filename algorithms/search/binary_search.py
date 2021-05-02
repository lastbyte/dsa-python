
class Solution:

    def binary_search(self, arr, target):
        return self.binary_search_util(arr,0,len(arr)-1,target)

    def binary_search_util(self, array, start, end, target):
        if start <= end:
            mid = int(start + ((end - start)/2))
            if array[mid] == target:
                return mid
            if array[mid] > target:
                return self.binary_search_util(array, start, mid-1, target)
            else:
                return self.binary_search_util(array, mid+1, end, target)
        return False


if __name__ == "__main__":

    arr = [1,2,3,4,5,6,7,8,9]
    solution = Solution()
    result = solution.binary_search(arr,9)
    print(result)
