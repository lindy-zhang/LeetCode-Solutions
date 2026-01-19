Easy/minimum-absolute-difference-in-bst.py

# Notes:
# - BST
# - DFS (in order traversal)

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def in_order(node, arr):
            if not node:
                return
            in_order(node.left, arr)
            arr.append(node.val)
            in_order(node.right, arr)
        in_order(root, arr)
        
        min_diff = float("inf")
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < min_diff:
                min_diff = diff
        
        return min_diff
