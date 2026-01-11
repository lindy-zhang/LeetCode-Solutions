Easy/two-sum.py

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Pair each value with its original index
        arr = [(val, idx) for idx, val in enumerate(nums)]
        print(arr)
        # Sort by value, NOT by index
        arr.sort(key=lambda x: x[0])
        print(arr)
        left = 0
        right = len(arr) - 1
        
        while left < right:
            tot = arr[left][0] + arr[right][0]
            
            if tot == target:
                return [arr[left][1], arr[right][1]]
            if tot < target:
                left += 1
            else:
                right -= 1
