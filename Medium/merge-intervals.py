Medium/merge-intervals.py

# Notes:
# - Array manipulation

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time: O(n log n)
        # Space: O(n)

        # Sort the intervals by their start time
        # Ensures that if two intervals overlap, they will be adjacent
        intervals.sort(key = lambda interval: interval[0]) 
        merged = []

        # Iterate through each interval
        for interval in intervals:
            # If merged is empty (starting at the 1st interval) OR
            # If the end of the last interval we added (merged[-1][1]) 
            # is less than the start of the current interval (interval[0]), there is no overlap.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else: # Overlap
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        return merged
