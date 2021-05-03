'''
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.
'''
class Solution:

    def generate_permutations(self,nums):
        permutations=[]
        self.generate_permutations_util(nums,0, len(nums)-1,permutations)
        return permutations


    def generate_permutations_util(self,nums,left, right, permutations):
        if left == right:
            permutations.append(nums.copy())
        for i in range(left, right+1):
            nums[left], nums[i] = nums[i], nums[left]
            self.generate_permutations_util(nums, left+1, right, permutations)
            nums[left], nums[i] = nums[i], nums[left]


if __name__ == "__main__":
    permutations = []
    nums=[1,1,3]
    solution = Solution()
    result = solution.generate_permutations(nums)
    print(result)
