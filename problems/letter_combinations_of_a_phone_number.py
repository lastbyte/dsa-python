'''Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
'''


class Solution:
    def letterCombinations(self, digits: str):
        #define letter map
        letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        totalCombinations = 1
        combinations = []
        for c in digits:
            if len(combinations) == 0:
                combinations = letter_map[c]
            else:
                tmp_combinations = combinations.copy()
                combinations = []
                for elem in tmp_combinations:
                    combinations += [elem + char for char in letter_map[c]]

        return combinations

    def reverseLetterCombination(self, s: str):
        letter_map = {
            'a': '2',
            'b': '2',
            'c': '2',
            'd': '3',
            'e': '3',
            'f': '3',
            'g': '4',
            'h': '4',
            'i': '4',
            'j': '5',
            'k': '5',
            'l': '5',
            'm': '6',
            'n': '6',
            'o': '6',
            'p': '7',
            'q': '7',
            'r': '7',
            's': '7',
            't': '8',
            'u': '8',
            'v': '8',
            'w': '9',
            'x': '9',
            'y': '9',
            'z': '9'
        }

        return ''.join([letter_map[c] for c in s])


if __name__ == "__main__":
    solution = Solution()
    digits = "2222"
    result = solution.letterCombinations(digits)
    print(result)P
    result = solution.reverseLetterCombination('baba')
    print(result)