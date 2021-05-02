
class Solution:
    def find_positions(self,nums: [int], target: int) -> [int]:

        if nums is None or len(nums) == 0 :
            return [-1,-1]

        left, right = 0, len(nums)-1

        index = self.binary_search(nums, left, right, target)

        if index is False:
            return [-1,-1]

        left_bound, right_bound = index, index

        while left_bound-1 >= 0 and nums[left_bound-1] == target:
            left_bound = self.binary_search(nums, 0, left_bound-1,target)


        while right_bound + 1 <= right and nums[right_bound+1] == target:
            right_bound = self.binary_search(nums, right_bound+1,right,target)

        return [left_bound,right_bound]


    def binary_search(self, array, start, end, target):
        if start <= end:
            mid = int(start + ((end - start) / 2))
            if array[mid] == target:
                return mid
            if array[mid] > target:
                return self.binary_search(array, start, mid - 1, target)
            else:
                return self.binary_search(array, mid + 1, end, target)
        return False


if __name__ == "__main__":

    solution = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print( solution.find_positions(nums, target))

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(solution.find_positions(nums, target))

    nums = []
    target = 0
    print(solution.find_positions(nums, target))
    nums = [0,1,1,1,2,2,4,5,5,5,6,6,7,7,7,7,7,8,9,9,10]
    target = 5
    print(solution.find_positions(nums, target))

    nums = [ 1, 1, 2]
    target = 1
    print(solution.find_positions(nums, target))
