'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

link -> https://leetcode.com/problems/merge-intervals/
'''

class Solution:
    def merge_intervals(self,intervals):
        self.min_heapify(intervals,0)
        merged_intervals = []
        merged_intervals.append(intervals.pop(0))
        while len(intervals) > 0:
            self.min_heapify(intervals,0)
            next_interval = intervals.pop(0)
            prev_interval = merged_intervals.pop()
            if prev_interval[1] >= next_interval[0]:
                prev_interval[1] = next_interval[1] if next_interval[1] > prev_interval[1] else prev_interval[1]
                merged_intervals.append(prev_interval)
            else:
                merged_intervals.append(prev_interval)
                merged_intervals.append(next_interval)

        return merged_intervals


    def merge_intervals_1(self,intervals):
        intervals.sort(key=lambda interval: interval[0])
        merged_intervals = []
        merged_intervals.append(intervals.pop(0))
        index = 0
        while index < len(intervals):
            prev_interval = merged_intervals[len(merged_intervals)-1]
            can_be_merged = False
            max_y = prev_interval[1]
            while index < len(intervals) and prev_interval[1] >= intervals[index][0]:
                max_y = intervals[index][1] if intervals[index][1] > max_y else max_y
                index +=1
                can_be_merged = True
            if can_be_merged:
                index -=1
                prev_interval[1] = max_y
            else:
                merged_intervals.append(intervals[index])
            index+=1


        return merged_intervals




    def min_heapify(self, intervals, index):
        if intervals is None:
            return

        left = index * 2 + 1
        right = index * 2 + 2

        if left < len(intervals):
            self.min_heapify(intervals, left)

        if right < len(intervals):
            self.min_heapify(intervals, right)

        if left < len(intervals) and intervals[index][0] > intervals[left][0]:
            intervals[index], intervals[left] = intervals[left], intervals[index]

        if right < len(intervals) and intervals[index][0] > intervals[right][0]:
            intervals[index], intervals[right], = intervals[right], intervals[index]

if __name__ == "__main__":
    solution = Solution()
    result = solution.merge_intervals_1([[5, 5], [1, 3], [3, 5], [4, 6], [1, 1], [3, 3], [5, 6], [3, 3], [2, 4], [0, 0]])
    print(result)