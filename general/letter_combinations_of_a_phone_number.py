'''Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
'''

class Solution:
    def letterCombinations(self, digits: str):
        #define letter map
        letter_map = {"2" : ["a","b","c"],
                      "3" : ["d","e","f"],
                      "4" : ["g","h","i"],
                      "5" : ["j","k","l"],
                      "6" : ["m","n","o"],
                      "7" : ["p","q","r","s"],
                      "8" : ["t","u","v"],
                      "9" : ["w","x","y", "z"]
                      }
        totalCombinations = 1
        combinations = []
        for c in digits:
            if len(combinations) == 0:
                combinations = letter_map[c]
            else:
                tmp_combinations = combinations.copy()
                combinations=[]
                for elem in tmp_combinations:
                    combinations += [elem+char for char in letter_map[c]]

        return combinations


if __name__ == "__main__" :
    solution = Solution()
    digits = "2222"
    result = solution.letterCombinations(digits)
    print(result)