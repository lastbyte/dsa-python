'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8

'''
from pprint import pprint


def generate_paranthesis(n: int):
    return generate_parenthesis_util(n, 0, 0, [], "")


def generate_parenthesis_util(n, num_open, num_close, combinations,
                              current_combination):
    if n == num_open == num_close:
        combinations.append(current_combination)
    else:
        if num_open < n:
            generate_parenthesis_util(n, num_open + 1, num_close, combinations,
                                      current_combination + "(")
        if num_close < num_open:
            generate_parenthesis_util(n, num_open, num_close + 1, combinations,
                                      current_combination + ")")
    return combinations


combinations = generate_paranthesis(1)
print("num combinations : {} \n combinations : {}".format(len(combinations), combinations))