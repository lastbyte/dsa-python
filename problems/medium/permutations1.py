'''
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.
'''

class Solution:
    def generate_permutaions_wrapper(self,nums,left, right, permutations):
        self.generate_permutations(nums, left,right, permutations)
        return list(permutations.values())

    def generate_permutations(self, nums,left, right, permutations):

        if left == right :
            permutations[''.join(str(c) for c in nums)] = nums.copy()
        for i in range(left, right+1):
            nums[left], nums[i] = nums[i], nums[left]
            self.generate_permutations(nums, left+1, right, permutations)
            nums[left], nums[i] = nums[i], nums[left]



if __name__ == "__main__":
    permutations = {}
    nums=[1,1,3,3]
    solution = Solution()
    print(solution.generate_permutaions_wrapper(nums,0, len(nums)-1,permutations))