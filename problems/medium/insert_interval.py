'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals is sorted by intervals[i][0] in ascending order.
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105

link -> https://leetcode.com/problems/insert-interval/
'''
class Solution:
    def insert_interval(self,intervals , newInterval):
        if len(intervals) == 1:
            if intervals[0][0] < newInterval[0]:
                intervals = intervals + [newInterval]
            else:
                intervals = [newInterval] + intervals
        else:
            insert_index = self.get_insert_index(intervals, newInterval)
            intervals = intervals[:insert_index] + [newInterval] + intervals[insert_index:]
        return self.merge_intervals(intervals)

    def merge_intervals(self, intervals):
        merged_intervals = []
        merged_intervals.append(intervals.pop(0))
        index = 0
        while index < len(intervals):
            prev_interval = merged_intervals[len(merged_intervals) - 1]
            can_be_merged = False
            max_y = prev_interval[1]
            while index < len(intervals) and prev_interval[1] >= intervals[index][0]:
                max_y = intervals[index][1] if intervals[index][1] > max_y else max_y
                index += 1
                can_be_merged = True
            if can_be_merged:
                index -= 1
                prev_interval[1] = max_y
            else:
                merged_intervals.append(intervals[index])
            index += 1

        return merged_intervals

    def get_insert_index(self,intervals, new_interval):
        start = 0
        end = len(intervals)-1

        while start <= end:
            mid = start + (end - start)//2
            if intervals[mid][0] == new_interval[0] :
                return mid
            elif intervals[mid][0] < new_interval[0]:
                start = mid + 1
            else:
                end = mid - 1
        return end+1



if __name__ == "__main__":
    solution = Solution()
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    result = solution.insert_interval(intervals, newInterval)
    print(result)