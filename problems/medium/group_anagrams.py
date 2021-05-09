'''
Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

link -> https://leetcode.com/problems/group-anagrams/
'''


class Solution:
    def group_anagrams(self, strs):
        groups = {}
        for word in strs:
            word_hash = self.get_word_hash(word)
            if word_hash in groups:
                groups[word_hash].append(word)
            else:
                groups[word_hash] = [word]
        return list(groups.values())

    def group_anagrams_1(self, strs):
        groups = {}
        for word in strs:
            word_hash = ''.join(sorted(word))
            if word_hash in groups:
                groups[word_hash].append(word)
            else:
                groups[word_hash] = [word]
        return list(groups.values())

    def get_word_hash(self,word):
        word_map = {}
        word_hash = ''
        for i in range(97,123):
            word_map[chr(i)] = 0
        for index in range(len(word)):
            word_map[word[index]]+=1
        for key,value in word_map.items():
            word_hash.__add__(key).__add__(str(value))
        return word_hash



if __name__ == "__main__":
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.group_anagrams(strs)
    print(result)