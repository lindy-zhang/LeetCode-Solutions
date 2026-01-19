Medium/longest-consecutive-sequence.py

# Notes:
# - O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert nums to a set
        s = set(nums)
        max_len = 0
      
        for num in s:
            # Check if num is the start of the sequence
            if (num - 1) not in s:
                curr_num = num
                curr_len = 1
                while (curr_num + 1) in s:
                    curr_num += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len
