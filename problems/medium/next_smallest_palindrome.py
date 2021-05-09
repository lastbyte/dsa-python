'''
Given a number, find the next smallest palindrome larger than this number. 

Example 1:

input  = “2 3 5 4 5” 
output = “2 3 6 3 2”

Example 2:

input = “9 9 9”
output = “1 0 0 1”. 
The input is assumed to be an array. Every entry in array represents a digit in input number. Let the array be ‘num[]’ and size of array be ‘n’

link -> https://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/

'''


class Solution:
    '''
    Explanation :- 
        Brute force approach is to check for all the numbers from n+1 until we find a palindrome number 
    
    Time Complexity :- 
        Best Case :  
        Average Case :  
        Worst Case :  
    
    Space Complexity :- 
        Best Case :  
        Average Case : 
        Worst Case : 
    '''
    def next_smallest_palindrome(self, nums):
        found = False
        num_itr = nums.copy()
        self.add_one(num_itr)
        while not found:
            if self.is_palindrome(num_itr):
                found = True
            else:
                self.add(num_itr, 1)
        return num_itr

    def add(self, nums, to_add):
        carry = to_add
        for i in range(len(nums) - 1, -1, -1):
            sum_val = (nums[i] + carry)
            carry, nums[i] = sum_val // 10, sum_val % 10
        if carry > 0:
            nums.insert(0, carry)

    def is_palindrome(self, nums):
        for i in range(len(nums) // 2):
            if nums[i] != nums[len(nums) - i - 1]:
                return False
        return True

    def next_palindrome_1(self, nums):
        l = len(nums)

        only_nines = True
        for i in range(l):
            if nums[i] != 9:
                only_nines = False
                break

        if only_nines:
            self.add(nums, 2)
            return nums

        #odd length
        if l % 2 != 0:
            if self.is_palindrome(nums):
                self.increment_to_palindrome(nums)
                return nums
            else:
                i, j = l // 2 - 1, l // 2 + 1
                while nums[i] == nums[j]:
                    i -= 1
                    j += 1
                left = list(reversed(nums[0: i + 1]))
                right = nums[j:len(nums)]
                if self.gt(left, right):
                    self.copy_left_to_right(nums,i,j)
                    return nums
                else:
                    self.copy_left_to_right(nums,i,j)
                    self.increment_to_palindrome(nums)
                    return nums
        #even length
        else:
            if self.is_palindrome(nums):
                self.increment_to_palindrome(nums)
                return nums
            else:
                i, j = l // 2 - 1, l // 2
                while nums[i] == nums[j]:
                    i -= 1
                    j += 1
                left = list(reversed(nums[0: i + 1]))
                right = nums[j:len(nums)]
                if self.gt(left, right):
                    self.copy_left_to_right(nums,i,j)
                    return nums
                else:
                    self.copy_left_to_right(nums,i,j)
                    self.increment_to_palindrome(nums)
                    return nums


    def increment_to_palindrome(self, nums):
        l = len(nums)
        if l % 2 == 0:
            i, j = (l // 2) - 1, l // 2
        else:
            i = j = l // 2
        carry = 1
        while i >= 0 and j < l and carry > 0:
            if i == j:
                sum_val = nums[i] + carry
                nums[i], carry = sum_val % 10, sum_val // 10
            else:
                sum_val = nums[i] + carry
                nums[i], nums[
                    j], carry = sum_val % 10, sum_val % 10, sum_val // 10
            i -= 1
            j += 1
        return nums

    def gt(self, num1, num2):
        return str(''.join(map(str,num1))) > str(''.join(map(str,num2)))

    def copy_left_to_right(self, nums,i,j):
        l = len(nums)
        
        for index in range(i+1):
            nums[l-index-1] = nums[index]



if __name__ == "__main__":
    solution = Solution()
    result = solution.next_palindrome_1([2,3,5,4,5])
    print(result)