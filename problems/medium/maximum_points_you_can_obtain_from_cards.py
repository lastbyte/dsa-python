'''
There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 
Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
 

Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length

link -> https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

[30,88,33,37,18,77,54,73,31,88,93,25,18,31,71,8,97,20,98,16,65,40,18,25,13,51,59]
26
'''


class Solution:
    def maximum_points(self, card_points, k):
        return self.maximum_points_util(card_points, 0, len(card_points) - 1, k, 0)

    def maximum_points_util(self, card_points, start, end, k, points):
        if k == 0:
            return points
        else:
            return max(self.maximum_points_util(card_points, start + 1, end, k - 1, points + card_points[start]),
                       self.maximum_points_util(card_points, start, end - 1, k - 1, points + card_points[end]))

    def maximum_points_util_1(self, card_points, k):
        max_sum = 0
        sum_from_start = [0]
        sum_from_end = [0]
        for i in range(1, k+1):
            sum_from_start.append(sum_from_start[i-1] + card_points[i-1])
            sum_from_end.append(sum_from_end[i-1] + card_points[len(card_points)-i])
        for i in range(k+1):
            curr_sum = sum_from_end[i] + sum_from_start[k - i]
            if max_sum < curr_sum :
                max_sum = curr_sum
        return max_sum





if __name__ == "__main__":
    solution = Solution()
    card_points = [30,88,33,37,18,77,54,73,31,88,93,25,18,31,71,8,97,20,98,16,65,40,18,25,13,51,59]
    k = 26
    result = solution.maximum_points_util_1(card_points, k)
    print()
    print(result)
