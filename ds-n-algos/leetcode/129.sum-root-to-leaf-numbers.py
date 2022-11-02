# @author: yprakash

class Solution:
    # https://leetcode.com/submissions/detail/835571846/
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def add_sum(nums, number, node):
            number += str(node.val)
            if node.left:
                add_sum(nums, number, node.left)
            if node.right:
                add_sum(nums, number, node.right)
            elif not node.left:  # its leaf node
                # total_sum += int(number)
                nums.append(int(number))

        nums = []
        add_sum(nums, '', root)
        return sum(nums)
